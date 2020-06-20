from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import getenv
from flask_bcrypt import Bcrypt


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']=getenv('TEST_DB_URI')
app.config['SECRET_KEY']=getenv('TEST_SECRET_KEY')

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

