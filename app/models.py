from . import db

#database structure for profiles
class UserProfile(db.Model):

    __tablename__ = 'user_profiles'
	
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(80))
    last_name = db.Column(db.String(80))
    email = db.Column(db.String(80))
    bio = db.Column(db.String(250))
    location = db.Column(db.String(80))
    gender = db.Column(db.String(80))
    image = db.Column(db.String(200))
    date = db.Column(db.String(80))
	
    def __init__(self, first_name, last_name, email, bio, location, gender, image, date):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.bio = bio
        self.location = location
        self.gender = gender
        self.image = image
        self.date = date
	
    def get_id(self):
        try:
            return unicode(self.id)  # python 2 support
        except NameError:
            return str(self.id)  # python 3 support

    def __repr__(self):
        return '<User %r>' % (self.id)

