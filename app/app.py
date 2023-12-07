from os import getenv
from flask import Flask


app = Flask(__name__)
app.secret_key = getenv("SECRET_KEY")

from app import routes  # pylint: disable=unused-import
