from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = "o2jncK4p0w"
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://mxyqfwjpxasuzq:45624688156ed48fcaf2c6d6783965cf386f53b41672252d636f22085b4561c9@ec2-54-159-112-44.compute-1.amazonaws.com:5432/d29tl4l1srdj3u"
#app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:duttybug@localhost:5432/proj1"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True 
app.config['UPLOAD_FOLDER'] = './app/static/uploads'
db = SQLAlchemy(app)

app.config.from_object(__name__)
from app import views
