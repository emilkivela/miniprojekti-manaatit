from sqlalchemy.sql import text
from app.db_connection import db

def get_tags(user_id):
    tags = db.session.execute(
        text("SELECT * FROM tags WHERE user_id=:user_id"),
        {"user_id": user_id}).fetchall()
    db.session.commit()
    return tags

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