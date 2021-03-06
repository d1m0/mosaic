from mosaic import app, db, videos
from flask import render_template, flash, redirect, session, url_for, request, g
from flask_login import login_user, logout_user, current_user, login_required
from .forms import UploadForm
from .models import User, Submission
from . import videoSet
from json import dumps
import os
import time
import datetime

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

@app.route('/file_upload', methods=['GET', 'POST'])
def file_upload():
    res = { 'files' : [ ]}
    for f in request.files:
        file = request.files[f]
        app.logger.info(file.filename)
        ul_filename = videoSet.save(file)
        ui_full_filename = videoSet.path(ul_filename)
        app.logger.info(ul_filename + "," + ui_full_filename)
        size = os.path.getsize(ui_full_filename)
        res['files'].append({
            'name': file.filename,
            "size": size,
            "url": ul_filename });
    app.logger.info("Result: " + str(res))
    return dumps(res)

@app.route('/upload_submit', methods=['POST'])
def upload_submit():
    form = UploadForm();

    if form.validate_on_submit():
        u = User(first_name=form.first_name.data, last_name=form.last_name.data, email=form.email.data);
        # lastVisitDT = datetime.datetime.strptime(form.lastChildVisit.data, '%m/%d/%Y');
        [mth, yr] = [int(v) for v in form.lastChildVisit.data.split('/')]
        lastVisitDT = datetime.date(day=1, month=mth, year=yr)
        s = Submission(time=datetime.datetime.utcnow(),
                       submission_type=form.submission_type.data,
                       url=form.video_url.data,
                       author=u,
                       homeCountry=form.homeCountry.data,
                       homeCity=form.homeCity.data,
                       courtCountry=form.courtCountry.data,
                       courtCity=form.courtCity.data,
                       courtCosts=form.courtCosts.data,
                       lastChildVisit=lastVisitDT,
                       childVisitFrequency=form.childVisitFrequency.data,
                       numChildren=form.numChildren.data,
                       milestones=form.milestones.data,
                       related_submission=form.related_submission.data,
                       relation=form.relationship.data,
                       ip=request.remote_addr,
                       tags=form.tags.data,
                       other=form.other.data);

        db.session.add(u);
        db.session.add(s);
        db.session.commit();
        return dumps(form.errors)
    else:
        return dumps(form.errors)

@app.route('/mosaic')
def mosaic():
    return render_template('mosaic.html', title='Erased Families')


@app.route('/upload')
def upload():
    return render_template('upload.html',
        title='Upload a story',
        form = UploadForm())

@app.route('/done', methods=['GET'])
def done():
    return render_template('done.html',
        title='Done!')
