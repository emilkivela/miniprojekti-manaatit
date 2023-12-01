import os
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
from app.app import app
from sqlalchemy.sql import text


load_dotenv()   # take environment variables from .env

conn_str = os.environ['AZURE_POSTGRESQL_CONNECTIONSTRING']
conn_str_params = {pair.split('=')[0]: pair.split('=')[1] for pair in conn_str.split(' ')}

dbuser = conn_str_params['user']
dbpass = conn_str_params['password']
dbhost = conn_str_params['host']
dbname = conn_str_params['dbname']
DATABASE_URI = f"postgresql+psycopg2://{dbuser}:{dbpass}@{dbhost}/{dbname}"
app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE_URI
db = SQLAlchemy(app)

db.session.execute(text("DROP TABLE books"))
db.session.execute(text("DROP TABLE articles"))

class Books(db.Model):
    __tablename__= "books"
    id = db.Column(db.Integer, primary_key=True)
    refkey = db.Column(db.String(200), nullable=True)
    title = db.Column(db.String(200), nullable=True)
    author = db.Column(db.String(200), nullable=True)
    pubyear = db.Column(db.Integer, nullable=True)

class Articles(db.Model):
    __tablename__= "articles"
    id = db.Column(db.Integer, primary_key=True)
    refkey = db.Column(db.String(200), nullable=True)
    title = db.Column(db.String(200), nullable=True)
    author = db.Column(db.String(200), nullable=True)
    journal = db.Column(db.String(200), nullable=True)
    pubyear = db.Column(db.Integer, nullable=True)
    volume = db.Column(db.String(200), nullable=True)
    pages = db.Column(db.String(200), nullable=True)

with app.app_context():
    db.create_all()
