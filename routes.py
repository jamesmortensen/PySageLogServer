__author__ = 'jem'

import webapp2


class SagLogHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write('Hello SageLog!')


route_list = [

    webapp2.Route(r'/logs', handler='handlers.sage_log_handler.SageLogHandler:get', methods="GET")

]