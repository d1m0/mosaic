from mosaic import db

relationships = [ "erased_mom" ]

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    submissions = db.relationship('Submission', backref='author', lazy='dynamic')

class Submission(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    time = db.Column(db.DateTime)
    url = db.Column(db.String(1024), index=True, unique=True)
    author_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    country = db.Column(db.String(120), index=True, unique=True)
    city = db.Column(db.String(120), index=True, unique=True)
    relation = db.Column(db.Enum(*relationships), index=True, unique=True)
    ip = db.Column(db.String(128), index=True, unique=True)
