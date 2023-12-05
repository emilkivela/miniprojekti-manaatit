# pylint: disable=invalid-name
import sys
sys.path.append(".")
from app.app import app
from app.db_connection import db

class AppLibrary:
    def clear_database(self):
        with app.app_context():
            db.drop_all()
            db.create_all()
