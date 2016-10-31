# [START imports]
import os
import urllib

import jinja2
import webapp2

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)
# [END imports]


class LoginPage(webapp2.RequestHandler):
    def get(self):
        template = JINJA_ENVIRONMENT.get_template('loginMQ.html')
        self.response.out.write(template.render())

class Login(webapp2.RequestHandler):
    def get(self):
        template = JINJA_ENVIRONMENT.get_template('index.html')
        self.response.out.write(template.render())


# [START app]
app = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/index.html', Login)
], debug=True)
# [END app]
