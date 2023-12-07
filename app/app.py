from os import getenv
from flask import Flask


app = Flask(__name__)
app.secret_key = getenv("SECRET_KEY")
from app.db_connection import db

from app import routes
