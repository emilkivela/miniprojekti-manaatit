from sqlalchemy.sql import text
from app.db_connection import db


def get_articles():
    articles = db.session.execute(text("SELECT * FROM articles")).fetchall()
    db.session.commit()
    return articles

def key_in_articles(refkey):
    result = db.session.execute(
    text("SELECT EXISTS(SELECT 1 FROM articles WHERE refkey=:refkey)"), {"refkey": refkey})
    exists = result.scalar()
    return exists

def create_article(key, title, author, journal, year, volume, pages):
    sql = "INSERT INTO articles (refkey, title, author, journal, pubyear, volume, pages) "\
          "VALUES (:key, :title, :author, :journal, :year, :volume, :pages)"
    db.session.execute(text(sql), {"key": key, "title": title, "author": author, "journal": journal,
                                   "year": year, "volume": volume, "pages": pages})
    db.session.commit()

def delete_reference(refkey):
    sql = "DELETE FROM articles WHERE refkey=:refkey"
    db.session.execute(text(sql), {"refkey": refkey})
    db.session.commit()
    