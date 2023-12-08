import secrets
from sqlalchemy.sql import text
from werkzeug.security import generate_password_hash, check_password_hash
from flask import redirect, session
from app.db_connection import db

def login(username, password):
    sql = "SELECT id, password FROM users WHERE username=:username"
    result = db.session.execute(text(sql), {"username":username})
    user = result.fetchone()
    if user is not None and check_password_hash(user.password, password):
        session["username"] = username
        session["user_id"] = user.id
        session["csrf_token"] = secrets.token_hex(16)
        return True

    return False

def logout():
    if "username" in session.keys():
        del session["username"]
    return redirect("/login")


def register(username, password):
    if len(username) < 3:
        return "Username is too short (min. 3 characters)"

    if len(password) < 3:
        return "Password is too short (min. 3 characters)"

    sql = "SELECT * FROM users WHERE username = :username"
    result = db.session.execute(text(sql), {"username": username})
    user = result.fetchone()
    if user:
        return "Username already exists"
    password_hash = generate_password_hash(password)
    sql = "INSERT INTO users (username, password) VALUES (:username, :password)"
    db.session.execute(text(sql), {"username": username, "password": password_hash})
    db.session.commit()
    return None
