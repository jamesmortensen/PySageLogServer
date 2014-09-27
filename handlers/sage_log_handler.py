__author__ = 'jem'

#from handlers.base import AppHandler
import logging
import webapp2
import json
import urllib

from services.sage_log_service import SageLogService

log = logging.getLogger(__name__)

class SageLogHandler(webapp2.RequestHandler):
    def get(self):
        #self.response.write('Hello SageLog!')
        self.post(None)

    def post(self, logs):
        json_param = self.request.get('json')
        json_param = urllib.unquote(json_param)
        logs_data = json.loads(json_param)
        log.info(logs_data['message'])
        log_bundles = logs_data['message']['logBundles']
        callback = self.request.get('callback')
        log_storer = SageLogService()
        log.info(logs_data['message'])
        log.info(log_bundles[0]['logEntries'])
        log_storer.store(log_bundles)
        self.response.status = '200'
        if(callback == None):
            self.response.headers['content-type'] = 'application/json'
            self.response.write(json.dumps(json_param))
        else:
            self.response.headers['content-type'] = 'text/javascript'
            self.response.write(callback + '(' + json.dumps(json_param) + ');')
        #self.response.write('Hello SageLog! Here is where we will call the service layer')
