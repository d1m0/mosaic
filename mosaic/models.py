from mosaic import db

relationships = [ "erased_mom" ]
submission_types = [ "local", "external" ]

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), index=True)
    email = db.Column(db.String(120), index=True, unique=True)
    submissions = db.relationship('Submission', backref='author', lazy='dynamic')

class Submission(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    time = db.Column(db.DateTime)
    submission_type = db.Column(db.Enum(*submission_types), index=True)
    url = db.Column(db.String(1024), index=True)
    author_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    country = db.Column(db.String(120), index=True)
    city = db.Column(db.String(120), index=True)
    relation = db.Column(db.Enum(*relationships), index=True)
    ip = db.Column(db.String(128), index=True)
    other = db.Column(db.String(1000), index=True)
