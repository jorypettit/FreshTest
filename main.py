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


class LoginPage(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()
        if user:
            url = users.create_logout_url(self.request.uri)
            url_linktext = 'Logout'
        else:
            url = users.create_login_url(self.request.uri)
            url_linktext = 'Login'
        
        template_values = {
            'user': user,
            'url': url,
            'url_linktext': url_linktext,
        }
        
        template = JINJA_ENVIRONMENT.get_template('loginMQ.html')
        self.response.out.write(template.render(template_values))

class RegisterPage(webapp2.RegisterHandler):
    def get(self):
    
        template = JINJA_ENVIRONMENT.get_template('register.html')
        self.response.out.write(template.render())

# [START app]
app = webapp2.WSGIApplication([
    ('/', LoginPage)
    ('/', RegisterPage)
], debug=True)
# [END app]
