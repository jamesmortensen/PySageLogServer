__author__ = 'jem'

from google.appengine.ext import ndb


class LogEntry(ndb.Model):
    type = ndb.StringProperty()
    color = ndb.StringProperty()
    encoded_data = ndb.TextProperty()
    pathname = ndb.StringProperty()
    timestamp = ndb.DateTimeProperty(auto_now_add=True)