from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = "o2jncK4p0w"
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:duttybug@localhost:5432/proj1"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True 
app.config['UPLOAD_FOLDER'] = './app/static/uploads'
db = SQLAlchemy(app)

app.config.from_object(__name__)
from app import views
