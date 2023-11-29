from app.app import app
from flask_sqlalchemy import SQLAlchemy
import os
from flask_migrate import Migrate
from dotenv import load_dotenv

load_dotenv()   # take environment variables from .env

conn_str = os.environ['AZURE_POSTGRESQL_CONNECTIONSTRING']
print(conn_str[:10])
conn_str_params = {pair.split('=')[0]: pair.split('=')[1] for pair in conn_str.split(' ')}

DATABASE_URI = 'postgresql+psycopg2://{dbuser}:{dbpass}@{dbhost}/{dbname}'.format(
    dbuser=conn_str_params['user'],
    dbpass=conn_str_params['password'],
    dbhost=conn_str_params['host'],
    dbname=conn_str_params['dbname']
)
app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE_URI
db = SQLAlchemy(app)

migrate = Migrate(app, db)

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