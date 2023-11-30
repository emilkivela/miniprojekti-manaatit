from flask import Flask
from flask import redirect, render_template, request, send_file
from sqlalchemy.sql import text

app = Flask(__name__)

from app.db_connection import db
@app.route("/")
def index():
    result = db.session.execute(text("SELECT * FROM books"))
    books = result.fetchall()
    result = db.session.execute(text("SELECT * FROM articles"))
    articles = result.fetchall()
    return render_template("index.html", books=books, articles=articles)

@app.route("/new")
def new():
    return render_template("new.html")

@app.route("/download")
def download():
    path = 'esimerkki.txt'
    return send_file(path, as_attachment=True)

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

    sql = "INSERT INTO articles (refkey, title, author, journal, pubyear, volume, pages) "\
          "VALUES (:key, :title, :author, :journal, :year, :volume, :pages)"
    db.session.execute(text(sql), {"key": key, "title": title, "author": author, "journal": journal,
                                   "year": year, "volume": volume, "pages": pages})
    db.session.commit()
    return redirect("/")
