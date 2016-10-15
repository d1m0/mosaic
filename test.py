from mosaic.models import User, Submission;

for s in Submission.query.all():
    print s.time, s.author.name, s.author.email, s.country, s.city, s.url
