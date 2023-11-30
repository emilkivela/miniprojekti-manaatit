from sqlalchemy.sql import text
from app.app import app
from app.app import db

def test_opening_ref_creation_page(client):
    response = client.get("/new")
    assert b"Author" in response.data

def test_created_book_ref_is_in_database(client):
    with app.app_context():
        db.session.execute(text("TRUNCATE TABLE books"))
        db.session.commit()
        client.post("/create_book", data={
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
        sql = "INSERT INTO books (refkey, title, author, pubYear) "\
              "VALUES (:key, :title, :author, :year)"
        db.session.execute(text(sql), {"key": "MIKA", "title": "Sivullinen",
                                       "author": "Camus", "year": 1942})
        db.session.commit()
    response = client.get("/")
    assert b"Sivullinen" in response.data and b"Camus" in response.data and b"1942" in response.data


def test_create_book_ref_with_empty_fields(client):
    with app.app_context():
        db.session.execute(text("TRUNCATE TABLE books"))
        db.session.commit()

    response = client.post("/create_book", data={
        "key": "",
        "title": "",
        "author": "",
        "year": ""
    })

    print(f"Response Status Code: {response.status_code}")
    print(f"Response Data: {response.get_data(as_text=True)}")

    assert b'All fields must be filled' in response.get_data(as_text=True).encode('utf-8')

def test_create_book_ref_with_non_integer_year(client):
    with app.app_context():
        db.session.execute(text("TRUNCATE TABLE books"))
        db.session.commit()

    response = client.post("/create_book", data={
        "key": "jotain",
        "title": "jotain",
        "author": "jotain",
        "year": "jotain"
    })
    assert b'Year must be a number' in response.get_data(as_text=True).encode('utf-8')
