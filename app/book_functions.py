from sqlalchemy.sql import text
from app.db_connection import db


def get_books():
    books = db.session.execute(text("SELECT * FROM books")).fetchall()
    db.session.commit()
    return books

def key_in_books(refkey):
    result = db.session.execute(
    text("SELECT EXISTS(SELECT 1 FROM books WHERE refkey=:refkey)"), {"refkey": refkey})
    exists = result.scalar()
    return exists

def create_book(key, title, author, year):
    sql = "INSERT INTO books (refkey, title, author, pubYear) VALUES (:key, :title, :author, :year)"
    db.session.execute(text(sql), {"key": key, "title": title, "author": author, "year": year})
    db.session.commit()

def delete_reference(refkey):
    sql = "DELETE FROM books WHERE refkey=:refkey"
    db.session.execute(text(sql), {"refkey": refkey})
    db.session.commit()
