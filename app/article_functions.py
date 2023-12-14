from sqlalchemy.sql import text
from app.db_connection import db
from app import tag_functions

def get_articles(user_id):
    articles = db.session.execute(
        text("SELECT * FROM articles WHERE user_id=:user_id"), {"user_id": user_id}).fetchall()
    db.session.commit()
    for i in range(0, len(articles)):  # pylint: disable=consider-using-enumerate
        articles[i] = list(articles[i])
        if articles[i][9] is None:
            articles[i][9] = "–"
        else:
            articles[i][9] = tag_functions.get_tag(articles[i][9])[1]
    return articles

def get_article(article_id):
    sql = "SELECT * FROM articles WHERE id=:article_id"
    article = db.session.execute(
        text(sql), {"article_id": article_id}).fetchone()
    return article

def key_in_articles(refkey, user_id):
    result = db.session.execute(
        text("SELECT EXISTS(SELECT 1 FROM articles WHERE refkey=:refkey AND user_id=:user_id)"),
        {"refkey": refkey, "user_id": user_id})
    exists = result.scalar()
    return exists

def create_article(key, title, author, journal, year, volume, pages, user_id, tag_id):  # pylint: disable=too-many-arguments
    sql = "INSERT INTO articles"\
                "(refkey, title, author, journal, pubyear, volume, pages, user_id, tag_id) "\
          "VALUES (:key, :title, :author, :journal, :year, :volume, :pages, :user_id, :tag_id)"
    db.session.execute(text(sql), {"key": key, "title": title, "author": author, "journal": journal,
                                   "year": year, "volume": volume, "pages": pages,
                                    "user_id": user_id, "tag_id": tag_id})
    db.session.commit()

def delete_reference(refkey, user_id):
    sql = "DELETE FROM articles WHERE refkey=:refkey AND user_id=:user_id"
    db.session.execute(text(sql), {"refkey": refkey, "user_id": user_id})
    db.session.commit()

def update_article(article_id, refkey, title, author, journal, year, volume, pages, tag_id): # pylint: disable=too-many-arguments
    sql = "UPDATE articles SET refkey=:refkey, title=:title, author=:author, journal=:journal,"\
          "pubYear=:pubyear, volume=:volume, pages=:pages, tag_id=:tag_id "\
          "WHERE id=:article_id"
    db.session.execute(text(sql), {"article_id": article_id, "refkey": refkey, "title": title,
                                   "author": author, "journal":journal,"pubyear": year,\
                                   "volume": volume, "pages":pages, "tag_id": tag_id})
    db.session.commit()

def get_tag_id(article_id):
    sql = "SELECT tag_id FROM articles WHERE id=:article_id"
    tag_id = db.session.execute(
        text(sql), {"article_id": article_id}).fetchall()
    db.session.commit()
    if len(tag_id) > 0:
        return tag_id[0][0]
    return None
