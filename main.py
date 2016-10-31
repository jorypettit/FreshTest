# [START imports]
import os
import urllib

from google.appengine.api import users
from google.appengine.ext import ndb

import jinja2
import webapp2

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)
# [END imports]


class MainPage(webapp2.RequestHandler):
    def get(self):
        greetings = 'somestring'
        template_values = {
            'greetings': greetings,
        }
        template = JINJA_ENVIRONMENT.get_template('loginMQ.html')
        self.response.out.write(template.render(template_values))

# [START app]
app = webapp2.WSGIApplication([
    ('/', MainPage),
], debug=True)
# [END app]
