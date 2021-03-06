from urlparse import urlparse, parse_qs
# from .videos import YouTube
from . import videoSet
from wtforms.validators import regexp
from re import compile

from wtforms.validators import ValidationError


class YoutubeURL(object):
    def __init__(self, message=None):
        self.min = min
        self.max = max
        if not message:
            message = u'Field must be a valid Youtube URL.'
        self.message = message

    # assumes the field has already been checked as a url
    def __call__(self, form, field):
        print(field.data)
        dater = urlparse(field.data)
        if len(dater)>0:
            # print domain
            if not (dater.netloc == "www.youtube.com" or dater.netloc == "www.youtu.be"):
                raise ValidationError(self.message)

            query = parse_qs(dater.query)
            if 'v' not in query:
                raise ValidationError(u"Video unspecified")
            else:
                # todo: try catch on google http errors
                # try:
                yt_result = False #YouTube.videos().list(id=query['v'], part='snippet').execute()

                # todo: yt_result on success is a json, check if videos list is empty
                if yt_result:
                    raise ValidationError(u"Youtube video does not exist")

class FileExt(object):
    def __init__(self):
        self.message = "Extension must be one of " + ",".join(videoSet.extensions)
        self.re = compile(u'^[^\/\\\\]*\.(' + '|'.join(videoSet.extensions) + ')$')

    def __call__(self, form, field):
        print "Trying to validate ", field.data
        if (not self.re.match(field.data.filename)):
            raise ValidationError(u"Extension must be one of " + ",".join(videoSet.extensions))
