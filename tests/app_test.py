from app.app import app
from app.app import db
from sqlalchemy.sql import text

def test_opening_ref_creation_page(client):
    response = client.get("/new")
    assert b"Author" in response.data

def test_created_ref_is_in_database(client):
    with app.app_context():
        db.session.execute(text("TRUNCATE TABLE books"))
        db.session.commit()
        response = client.post("/create", data={
            "key": "MIKA",
            "title": "Jotain",
            "author": "Joku",
            "year": "2002"
        })
        result = db.session.execute(text("SELECT * FROM books"))
    ref = result.fetchone()
    assert ref[1] == "MIKA" and ref[2] == "Jotain" and ref[3] == "Joku" and ref[4] == 2002

def test_index_fetches_refs_from_database(client):
    with app.app_context():
        db.session.execute(text("TRUNCATE TABLE books"))
        db.session.commit()
        sql = "INSERT INTO books (refkey, title, author, pubYear) VALUES (:key, :title, :author, :year)"
        db.session.execute(text(sql), {"key": "MIKA", "title": "Sivullinen", "author": "Camus", "year": 1942})
        db.session.commit()
    response = client.get("/")
    assert b"Sivullinen" and b"Camus" and b"1942" in response.data