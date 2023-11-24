from flask import Flask
from os import getenv
from flask import Flask
from flask import redirect, render_template, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import text

#from app.db_connection import db

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql:///reftool"
db = SQLAlchemy(app)

@app.route("/")
def index():
    result = db.session.execute(text("SELECT * FROM books"))
    references = result.fetchall()
    return render_template("index.html", references=references)

@app.route("/new")
def new():
    return render_template("new.html")

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
