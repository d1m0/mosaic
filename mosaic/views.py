from mosaic import app, db, videos
from flask import render_template, flash, redirect, session, url_for, request, g
from flask_login import login_user, logout_user, current_user, login_required
from datetime import datetime
from .forms import UploadForm
from .models import User, Submission
from . import videoSet

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

@app.route('/instructions')
def instructions():
    return render_template('instructions.html',
        title='Instructions')

@app.route('/upload', methods=['GET', 'POST'])
def upload():
    form = UploadForm();

    if form.validate_on_submit() and 'video_url' in request.files:
        filename = videoSet.save(request.files['video_url'])
        u = User(name=form.name.data, email=form.email.data);
        s = Submission(time=datetime.utcnow(),
                       submission_type=form.submission_type.data,
                       url=filename,
                       author=u,
                       country=form.country.data,
                       city=form.city.data,
                       relation=form.relationship.data,
                       ip=request.remote_addr);
        #TODO(dimo): Add tags to db
        db.session.add(u);
        db.session.add(s);
        db.session.commit();
        return redirect(url_for('done'))

    return render_template('upload.html',
        title='Upload a story',
        form = form)

@app.route('/done', methods=['GET'])
def done():
    return render_template('done.html',
        title='Done!')
