import secrets
from io import BytesIO
from flask import Flask
from flask import redirect, render_template, request, send_file, session
from sqlalchemy.sql import text
from app.services.bibtex_service import BibtexService

app = Flask(__name__)
app.secret_key = secrets.token_urlsafe(16)


from app.db_connection import db
from app import users

@app.route("/")
def index():
    #if not "username" in session:
    #    return redirect("/login")
    result = db.session.execute(text("SELECT * FROM books"))
    books = result.fetchall()
    result = db.session.execute(text("SELECT * FROM articles"))
    articles = result.fetchall()
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
    result = db.session.execute(text("SELECT * FROM books"))
    books = result.fetchall()
    result = db.session.execute(text("SELECT * FROM articles"))
    articles = result.fetchall()

    bibtex_service = BibtexService(books, articles)
    bibtex_str = bibtex_service.generate_bibtex_str()

    return send_file(BytesIO(bytes(bibtex_str, "utf-8")),
                     as_attachment=True,
                     download_name="references.bib",
                     mimetype="application/x-bibtex"
                     )

def key_exists(key):

    result_books = db.session.execute(
    text("SELECT EXISTS(SELECT 1 FROM books WHERE refkey = :key)"), {"key": key})
    exists_books = result_books.scalar()

    result_articles = db.session.execute(
    text("SELECT EXISTS(SELECT 1 FROM articles WHERE refkey = :key)"), {"key": key})
    exists_articles = result_articles.scalar()

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

    sql = "INSERT INTO books (refkey, title, author, pubYear) VALUES (:key, :title, :author, :year)"
    db.session.execute(text(sql), {"key": key, "title": title, "author": author, "year": year})
    db.session.commit()
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

    sql = "INSERT INTO articles (refkey, title, author, journal, pubyear, volume, pages) "\
          "VALUES (:key, :title, :author, :journal, :year, :volume, :pages)"
    db.session.execute(text(sql), {"key": key, "title": title, "author": author, "journal": journal,
                                   "year": year, "volume": volume, "pages": pages})
    db.session.commit()
    return redirect("/")
