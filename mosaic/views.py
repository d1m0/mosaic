from mosaic import app, db, videos
from flask import render_template, flash, redirect, session, url_for, request, g
from flask_login import login_user, logout_user, current_user, login_required
from datetime import datetime
from .forms import UploadForm
from .models import User, Submission

@app.errorhandler(404)
def not_found_error(error):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_error(error):
    db.session.rollback()
    return render_template('500.html'), 500

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html',
        title='Home')

@app.route('/upload', methods=['GET', 'POST'])
def upload():
    form = UploadForm();
    if form.validate_on_submit():
        filename = videos.save(request.files['video'])
        flash('Your changes have been saved as ' + filename)
        return redirect(url_for('done'))

    return render_template('upload.html',
        title='Upload a story',
        form = form)


@app.route('/done', methods=['GET'])
def done():
    return render_template('done.html',
        title='Done!')
