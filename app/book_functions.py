from sqlalchemy.sql import text
from app.db_connection import db
from app import tag_functions


def get_books(user_id):
    books = db.session.execute(
        text("SELECT * FROM books WHERE user_id=:user_id"), {"user_id": user_id}).fetchall()
    db.session.commit()
    for i in range(0, len(books)):  # pylint: disable=consider-using-enumerate
        books[i] = list(books[i])
        if books[i][7] is None:
            books[i][7] = "–"
        else:
            books[i][7] = tag_functions.get_tag(books[i][7])[1]
    return books

def get_book(book_id):
    sql = "SELECT * FROM books WHERE id=:book_id"
    book = db.session.execute(
        text(sql), {"book_id": book_id}).fetchone()
    return book

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

def update_book(book_id, refkey, title, author, year, publisher, tag_id): # pylint: disable=too-many-arguments
    sql = "UPDATE books SET refkey=:refkey, title=:title, author=:author, pubyear=:pubyear,"\
        " publisher=:publisher, tag_id=:tag_id WHERE id=:book_id;"
    db.session.execute(text(sql), {"refkey": refkey, "title": title, "author": author,\
                                   "pubyear": year, "publisher": publisher,\
                                   "tag_id": tag_id, "book_id": book_id})
    db.session.commit()

def get_tag_id(book_id):
    sql = "SELECT tag_id FROM books WHERE id=:book_id"
    tag_id = db.session.execute(
        text(sql), {"book_id": book_id}).fetchall()
    db.session.commit()
    if len(tag_id) > 0:
        return tag_id[0][0]
    return None
