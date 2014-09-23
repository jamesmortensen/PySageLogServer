__author__ = 'jem'

import logging
import webapp2
from models.sage_log_model import SageLogModel

log = logging.getLogger(__name__)

class SageLogService():
    def store(self, log_bundles):
        log.info('store the logs by calling the model layer %s', log_bundles)
        sage_log_model = SageLogModel()
        sage_log_model.store(log_bundles)

