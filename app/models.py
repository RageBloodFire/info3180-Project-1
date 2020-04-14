from . import db

#database structure for profiles
class UserProfile(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(80))
    last_name = db.Column(db.String(80))
	email = db.Column(db.String(80))
    bio = db.Column(db.String(80))
	location = db.Column(db.String(80))
	gender = db.Column(db.String(80))
	image = db.Column(db.String(80))
	creation_date = db.Column(db.String(200))

