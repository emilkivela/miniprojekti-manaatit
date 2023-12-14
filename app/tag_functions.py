from sqlalchemy.sql import text
from app.db_connection import db

def get_tags():
    sql = "SELECT * FROM tags;"
    tags = db.session.execute(text(sql)).fetchall()
    db.session.commit()
    return tags

def get_tag(tag_id):
    sql = "SELECT name FROM tags WHERE id=:tag_id"
    tag = db.session.execute(text(sql), {"tag_id": tag_id}).fetchall()[0]
    db.session.commit()
    return tag

def tag_exists(tag_name):
    result = db.session.execute(
        text("SELECT EXISTS(SELECT 1 FROM tags WHERE name=:tag_name)"),
        {"tag_name": tag_name})
    exists = result.scalar()
    return exists

def create_tag(name):
    sql = "INSERT INTO tags (name) VALUES (:name)"
    db.session.execute(text(sql), {"name": name})
    db.session.commit()

def add_tag_to_book(book_key, tag_name):
    tag = db.session.execute(
        text("SELECT id FROM tags WHERE name=:tag_name"),
        {"tag_name": tag_name}).fetchone()

    sql = "UPDATE books SET tag_id=:tag_id WHERE key=:book_key"
    db.session.execute(text(sql), {"tag_id": tag.id, "book_key": book_key})
    db.session.commit()

def add_tag_to_article(article_key, tag_name):
    tag = db.session.execute(
        text("SELECT id FROM tags WHERE name=:tag_name"),
        {"tag_name": tag_name}).fetchone()

    sql = "UPDATE articles SET tag_id=:tag_id WHERE key=:article_key"
    db.session.execute(text(sql), {"tag_id": tag.id, "article_key": article_key})
    db.session.commit()
