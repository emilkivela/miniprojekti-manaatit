from io import BytesIO
from functools import wraps
from flask import redirect, render_template, request, send_file, session, flash
from app.services.bibtex_service import BibtexService
from app.app import app
from app import users, book_functions, article_functions, tag_functions

def login_required(f):
    @wraps(f)
    def login_check(*args, **kwargs):
        if 'username' not in session:
            return redirect("/login")
        return f(*args, **kwargs)
    return login_check

@app.route("/")
@login_required
def index():
    user_id = session.get('user_id')
    books = book_functions.get_books(user_id)
    articles = article_functions.get_articles(user_id)
    return render_template("index.html", books=books, articles=articles)

@app.route("/login", methods=["GET", "POST"])
def login():
    if "username" in session:
        return redirect("/")

    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        logged_in_succesfully = users.login(username, password)
        if logged_in_succesfully:
            return redirect("/")
        flash("Wrong username or password")
    return render_template("login.html")

@app.route("/logout")
def logout():
    users.logout()
    return redirect("/")

@app.route("/register")
def register():
    return render_template("register.html")

@app.route("/send_registration", methods=["POST"])
def send_registration():
    username = request.form["username"]
    password = request.form["password"]
    error = users.register(username, password)
    if error:
        return render_template("register.html", error = error)
    return redirect("/")

@app.route("/new")
@login_required
def new():
    tags = tag_functions.get_tags()
    return render_template("new.html", tags=tags)

@app.route("/download")
@login_required
def download():
    books = book_functions.get_books(session.get('user_id'))
    articles = article_functions.get_articles(session.get('user_id'))

    bibtex_service = BibtexService(books, articles)
    bibtex_str = bibtex_service.generate_bibtex_str()

    return send_file(BytesIO(bytes(bibtex_str, "utf-8")),
                     as_attachment=True,
                     download_name="references.bib",
                     mimetype="application/x-bibtex"
                     )

def key_exists(key):
    user_id = session.get('user_id')
    exists_books = book_functions.key_in_books(key, user_id)
    exists_articles = article_functions.key_in_articles(key, user_id)
    return exists_books or exists_articles

@app.route("/create_book", methods=["POST"])
@login_required
def create_book():
    key = request.form["key"]
    title = request.form["title"]
    author = request.form["author"]
    year = request.form["year"]
    publisher = request.form["publisher"]
    user_id = session.get('user_id')
    tag_id = request.form["tag"]
    if request.form["tag"] == "0":
        tag_id = None

    if not key or not title or not author or not year or not publisher:
        flash("All fields must be filled")
        return render_template("new.html")

    if not year.isdigit():
        flash("Year must be a number")
        return render_template("new.html")

    if key_exists(key):
        flash("Key already exists")
        return render_template("new.html")

    book_functions.create_book(key, title, author, year, publisher, user_id, tag_id)
    return redirect("/")

@app.route("/create_article", methods=["POST"])
@login_required
def create_article():
    key = request.form["key"]
    title = request.form["title"]
    author = request.form["author"]
    journal = request.form["journal"]
    year = request.form["year"]
    volume = request.form["volume"]
    pages = request.form["pages"]
    user_id = session.get('user_id')
    tag_id = request.form["tag"]
    if request.form["tag"] == "0":
        tag_id = None

    if not key or not title or not author or not journal:
        flash("All fields must be filled")
        return render_template("new.html")

    if not year or not volume or not pages:
        flash("All fields must be filled")
        return render_template("new.html")

    if not year.isdigit():
        flash("Year must be a number")
        return render_template("new.html")

    if key_exists(key):
        flash("Key already exists")
        return render_template("new.html")

    article_functions.create_article(
        key,
        title,
        author,
        journal,
        year,
        volume,
        pages,
        user_id,
        tag_id
        )

    return redirect("/")

@app.route("/remove_reference", methods=["POST","GET"])
@login_required
def remove_reference():
    user_id = session.get('user_id')
    refkey = request.form["refkey"]
    if book_functions.key_in_books(refkey, user_id):
        book_functions.delete_reference(refkey, user_id)
        return redirect("/")
    if article_functions.key_in_articles(refkey, user_id):
        article_functions.delete_reference(refkey, user_id)
        return redirect("/")
    flash("Key does not exist")
    books = book_functions.get_books(session.get('user_id'))
    articles = article_functions.get_articles(session.get('user_id'))
    return render_template("index.html", books=books, articles=articles)

@app.route("/edit_book/<id>", methods=["POST","GET"])
@login_required
def edit_book():
    book_id = id
    book = book_functions.get_book(book_id)
    tag_id = book_functions.get_tag_id(book_id)
    tag = None
    if tag_id is not None:
        tag = tag_functions.get_tag(tag_id)
    tags = tag_functions.get_tags()
    return render_template("edit_book.html", book=book, tags=tags, tag=tag)


@app.route("/update_book", methods=["POST", "GET"])
@login_required
def update_book():
    refkey = request.form["refkey"]
    title = request.form["title"]
    author = request.form["author"]
    year = request.form["year"]
    publisher = request.form["publisher"]
    book_id = request.form["book_id"]
    tag_id = request.form["tag"]
    if request.form["tag"] == "0":
        tag_id = None

    if not refkey or not title or not author or not year or not publisher:
        flash("All fields must be filled")
        return render_template("edit_book.html")

    if not year.isdigit():
        flash("Year must be a number")
        return render_template("edit_book.html")

    book_functions.update_book(book_id, refkey, title, author, year, publisher, tag_id)
    return redirect("/")

@app.route("/edit_article/<key>", methods=["POST", "GET"])
@login_required
def edit_article(key):
    user_id = session.get("user_id")
    if article_functions.key_in_articles(key, user_id):
        if request.method == "POST":
            refkey = request.form["refkey"]
            title = request.form["title"]
            author = request.form["author"]
            journal = request.form["journal"]
            year = request.form["year"]
            volume = request.form["volume"]
            pages = request.form["pages"]
            tag_id = None

            if not refkey or not title or not author or not journal:
                flash("All fields must be filled")
                return render_template("edit_article.html")

            if not year or not volume or not pages:
                flash("All fields must be filled")
                return render_template("edit_article.html")

            if not year.isdigit():
                flash("Year must be a number")
                return render_template("edit_article.html")

            article_functions.update_article(key, refkey, title, author, journal,
                                              year, volume, pages, user_id, tag_id
                                            )
            return redirect("/")
    else:
        return redirect("/")

    return render_template("edit_article.html", key=key)

@app.route("/create_tags")
@login_required
def create_tags():
    return render_template("tag.html")

@app.route("/create_tag", methods=["POST"])
@login_required
def create_tag():
    name = request.form["name"]

    if tag_functions.tag_exists(name):
        flash("Tag already exists")
        return render_template("tag.html")

    tag_functions.create_tag(name)

    return render_template("tag.html")

@app.route('/add_tag_to_book', methods=['POST'])
@login_required
def add_tag_to_book():
    book_key = request.form.get('book_key')
    tag_name = request.form.get('tag_name')

    if not book_key or not tag_name:
        flash("All fields must be filled")
        return render_template("tag.html")

    tag_functions.add_tag_to_book(book_key, tag_name)

    return render_template("tag.html")

@app.route('/add_tag_to_article', methods=['POST'])
@login_required
def add_tag_to_article():
    article_key = request.form.get('book_key')
    tag_name = request.form.get('tag_name')

    if not article_key or not tag_name:
        flash("All fields must be filled")
        return render_template("tag.html")

    tag_functions.add_tag_to_book(article_key, tag_name)

    return render_template("tag.html")
