__author__ = 'jem'

import logging
import LogBundle
from LogEntry import LogEntry

from google.appengine.ext import ndb

log = logging.getLogger(__name__)


class SageLogModel():
    def store(self, log_bundles):
        log.debug('store the logs by calling the model layer')
        log.debug(log_bundles)
        log_entries = log_bundles[0]['logEntries']   #.logEntries.tolist()
        log.info(log_entries)

        for log_entry in log_entries:
            log.info(log_entry)
            log.info(log_entry)
            ndb_log_entry = LogEntry(type='debug')
            ndb_log_entry.type = log_entry['type']
            ndb_log_entry.color = log_entry['color']
            ndb_log_entry.encoded_data = log_entry['encodedData']
            ndb_log_entry.pathname = log_entry['pathname']
            #ndb_log_entry.timestamp = log_entry['timestamp']
                                      #log_entries=[])
            ndb_log_entry.put()





#def get(self, log_id):
#log.debug('retrieve the logs for logid ' + log_id)