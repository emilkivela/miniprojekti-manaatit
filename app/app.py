from flask import Flask
from os import getenv
from flask import Flask
from flask import redirect, render_template, request, send_file
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import text

app = Flask(__name__)

from app.db_connection import db
@app.route("/")
def index():
    result = db.session.execute(text("SELECT * FROM books"))
    references = result.fetchall()
    return render_template("index.html", references=references)

@app.route("/new")
def new():
    return render_template("new.html")

@app.route("/download")
def download():
    path = 'esimerkki.txt'
    return send_file(path, as_attachment=True)

@app.route("/create", methods=["POST"])
def create():
    key = request.form["key"]
    title = request.form["title"]
    author = request.form["author"]
    year = request.form["year"]
    sql = "INSERT INTO books (refkey, title, author, pubYear) VALUES (:key, :title, :author, :year)"
    db.session.execute(text(sql), {"key": key, "title": title, "author": author, "year": year})
    db.session.commit()
    return redirect("/")
