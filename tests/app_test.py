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
            "title": "Jotain",
            "author": "Joku",
            "year": "2002"
        })
        result = db.session.execute(text("SELECT * FROM books"))
    ref = result.fetchone()
    assert ref[1] == "Jotain" and ref[2] == "Joku" and ref[3] == 2002
