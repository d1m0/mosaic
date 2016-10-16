from mosaic import db

relationships = map( lambda name: "erased_" + name, [
        "mom", "dad", "sister", "brother", "grandparent", "aunt_or_uncle",
        "cousin", "other_family", "step_family", "friend"
    ])
submission_types = [ "local", "external" ]

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(120), index=True)
    last_name = db.Column(db.String(120), index=True)
    email = db.Column(db.String(120), index=True, unique=True)
    submissions = db.relationship('Submission', backref='author', lazy='dynamic')

class Submission(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    time = db.Column(db.DateTime)

    lastChildVisit = db.Column(db.DateTime)
    childVisitFrequency = db.Column(db.Integer)
    numChildren = db.Column(db.Integer)

    submission_type = db.Column(db.Enum(*submission_types), index=True)

    url = db.Column(db.String(1024), index=True)

    author_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    homeCountry = db.Column(db.String(120), index=True)
    homeCity = db.Column(db.String(120), index=True)

    courtCountry = db.Column(db.String(120), index=True)
    courtCity = db.Column(db.String(120), index=True)

    courtCosts = db.Column(db.Integer)

    relation = db.Column(db.Enum(*relationships), index=True)

    ip = db.Column(db.String(128), index=True)

    tags = db.Column(db.String(1024), index=True)

    milestones = db.Column(db.String(1024), index=True)

    related_submission = db.Column(db.String(512), index=True)

    other = db.Column(db.String(1000), index=True)
