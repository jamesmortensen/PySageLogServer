__author__ = 'jem'

from google.appengine.ext import ndb

import LogEntry


class LogBundle(ndb.Model):
    bundle_name = ndb.StringProperty()
    #log_entries = ndb.StructuredProperty(LogEntry)