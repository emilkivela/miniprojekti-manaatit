from io import BytesIO
from flask import redirect, render_template, request, send_file, session
from app.services.bibtex_service import BibtexService
from app.app import app
from app import users, book_functions, article_functions


@app.route("/")
def index():
    #if not "username" in session:
    #    return redirect("/login")
    books = book_functions.get_books()
    articles = article_functions.get_articles()
    return render_template("index.html", books=books, articles=articles)

@app.route("/login", methods=["GET", "POST"])
def login():
    if "username" in session:
        return redirect("/")
    error = None
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        logged_in_succesfully = users.login(username, password)
        if logged_in_succesfully:
            return redirect("/")
        error = "Wrong username or password"
    return render_template("login.html", error=error)

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
def new():
    return render_template("new.html")

@app.route("/download")
def download():
    books = book_functions.get_books()
    articles = article_functions.get_articles()

    bibtex_service = BibtexService(books, articles)
    bibtex_str = bibtex_service.generate_bibtex_str()

    return send_file(BytesIO(bytes(bibtex_str, "utf-8")),
                     as_attachment=True,
                     download_name="references.bib",
                     mimetype="application/x-bibtex"
                     )

def key_exists(key):
    exists_books = book_functions.key_in_books(key)
    exists_articles = article_functions.key_in_articles(key)
    return exists_books or exists_articles

@app.route("/create_book", methods=["POST"])
def create_book():
    key = request.form["key"]
    title = request.form["title"]
    author = request.form["author"]
    year = request.form["year"]

    if not key or not title or not author or not year:
        return render_template("new.html", error="All fields must be filled")

    if not year.isdigit():
        return render_template("new.html", error="Year must be a number")

    if key_exists(key):
        return render_template("new.html", error="Key already exists")

    book_functions.create_book(key, title, author, year)
    return redirect("/")

@app.route("/create_article", methods=["POST"])
def create_article():
    key = request.form["key"]
    title = request.form["title"]
    author = request.form["author"]
    journal = request.form["journal"]
    year = request.form["year"]
    volume = request.form["volume"]
    pages = request.form["pages"]

    if not key or not title or not author or not journal:
        return render_template("new.html", error="All fields must be filled")

    if not year or not volume or not pages:
        return render_template("new.html", error="All fields must be filled")

    if not year.isdigit():
        return render_template("new.html", error="Year must be a number")

    if key_exists(key):
        return render_template("new.html", error="Key already exists")

    article_functions.create_article(key, title, author, journal, year, volume, pages)
    return redirect("/")

@app.route("/remove_reference", methods=["POST","GET"])
def remove_reference():
    refkey = request.form["refkey"]
    if book_functions.key_in_books(refkey):
        book_functions.delete_reference(refkey)
        return redirect("/")
    if article_functions.key_in_articles(refkey):
        article_functions.delete_reference(refkey)
        return redirect("/")
    return redirect("/")
