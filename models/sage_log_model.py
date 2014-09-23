__author__ = 'jem'

import logging
import LogBundle
#import LogEntry

from google.appengine.ext import ndb

log = logging.getLogger(__name__)


class SageLogModel():
    def store(self, log_bundles):
        log.debug('store the logs by calling the model layer')
        #log_entries = log_bundles['logEntries']   #.logEntries.tolist()
        #log.info(log_entries)
        for log_bundle in log_bundles:
            log.info(log_bundle)
            #log.info(log_bundle.logEntries)
            ndb_log_bundle = LogBundle()
            ndb_log_bundle.bundle_name = 'default'
            #                          log_entries=[])
            #ndb_log_bundle.put()





#def get(self, log_id):
#log.debug('retrieve the logs for logid ' + log_id)