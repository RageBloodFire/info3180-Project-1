"""
Flask Documentation:     http://flask.pocoo.org/docs/
Jinja2 Documentation:    http://jinja.pocoo.org/2/documentation/
Werkzeug Documentation:  http://werkzeug.pocoo.org/documentation/
This file creates your application.
"""
import os, datetime
from app import app, db
from flask import render_template, request, redirect, url_for, flash, abort
from werkzeug.utils import secure_filename
from app.forms import AddProfile
from app.models import UserProfile

UPLOAD_FOLDER = './app/static/uploads'

###
# Routing for your application.
###

@app.route('/')
def home():
    """Render website's home page."""
    return render_template('home.html')


@app.route('/about/')
def about():
    """Render the website's about page."""
    return render_template('about.html', name="Robert Fernandez")


@app.route('/profile', methods=['POST', 'GET'])
def profile():

    addprof = AddProfile()

    # Validate profile info on submit
    if request.method == 'POST':
	
        # Get image data and save to upload folder
        pic = request.files['photo']
        filename = secure_filename(pic.filename)
        pic.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
		
		# Get the rest of the profile data
        fname = addprof.fname.data
        lname = addprof.lname.data
        email = addprof.email.data
        location = addprof.location.data
        bio = addprof.bio.data
        gender = addprof.gender.data
        x = datetime.date.today()
        date = x.strftime("%B %d %Y") 

		
		# Save data to database
        newUser = UserProfile(first_name=fname, last_name=lname, email=email, bio=bio, location=location, gender=gender, image=filename, date=date)
        db.session.add(newUser)
        db.session.commit()
		
        profiles = UserProfile.query.all()
        flash('Profile Added', 'success')
        return redirect(url_for('profiles', profiles=profiles))

    return render_template('profile.html', form=addprof)
    

@app.route('/profiles', methods=['POST', 'GET'])
def profiles():

    profiles = UserProfile.query.all()
    return render_template('profiles.html', profiles=profiles)


@app.route('/profile/<user_id>', methods=['GET'])
def user(user_id):
	
    user = UserProfile.query.filter_by(id=user_id).first()
	
    if request.method == 'POST':
        return redirect(url_for('user', user=user))
		
    return render_template('user.html', user=user)
	

def get_uploaded_images():
    rootdir = os.getcwd()
    list = []
    for subdir, dirs, files in os.walk(rootdir + '/app/static/uploads/'):
        for file in files:
            list.append(file)
        return list




###
# The functions below should be applicable to all Flask apps.
###

# Flash errors from the form if validation fails
def flash_errors(form):
    for field, errors in form.errors.items():
        for error in errors:
            flash(u"Error in the %s field - %s" % (
                getattr(form, field).label.text,
                error
), 'danger')

@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port="8080")
