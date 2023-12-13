from sqlalchemy.sql import text
from app.db_connection import db


def get_books(user_id):
    books = db.session.execute(
        text("SELECT * FROM books WHERE user_id=:user_id"), {"user_id": user_id}).fetchall()
    db.session.commit()
    return books

def key_in_books(refkey, user_id):
    result = db.session.execute(
        text("SELECT EXISTS(SELECT 1 FROM books WHERE refkey=:refkey AND user_id=:user_id)"),
        {"refkey": refkey, "user_id": user_id})
    exists = result.scalar()
    return exists

def create_book(key, title, author, year, publisher, user_id, tag_id): # pylint: disable=too-many-arguments
    sql = "INSERT INTO books (refkey, title, author, pubYear, publisher, user_id, tag_id) "\
          "VALUES (:key, :title, :author, :year, :publisher, :user_id, :tag_id)"
    db.session.execute(text(sql), {"key": key, "title": title, "author": author, "year": year,\
                                   "publisher": publisher, "user_id": user_id, "tag_id": tag_id})
    db.session.commit()

def delete_reference(refkey, user_id):
    sql = "DELETE FROM books WHERE refkey=:refkey AND user_id=:user_id"
    db.session.execute(text(sql), {"refkey": refkey, "user_id": user_id})
    db.session.commit()

def update_book(og_key, refkey, title, author, year, publisher, user_id, tag_id): # pylint: disable=too-many-arguments
    sql = "UPDATE books SET refkey=:refkey, title=:title, author=:author, pubYear=:pubYear, publisher=:publisher, tag_id=:tag_id WHERE refkey=:og_key AND user_id=:user_id"
    db.session.execute(text(sql), {"refkey": refkey, "title": title, "author": author, "pubYear": year,\
                                   "publisher": publisher, "user_id": user_id, "tag_id": tag_id, "og_key":og_key})
    db.session.commit()
