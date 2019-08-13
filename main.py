import webapp2
import jinja2
import os
import json
from google.appengine.api import urlfetch
from urllib import urlencode
import logging

from pprint import pformat

jinja_env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

class MainPageHandler(webapp2.RequestHandler):
    def get(self):

        base_url = "https://fourtonfish.com/hellosalut/?mode=auto";
        response = urlfetch.fetch(base_url, method=urlfetch.POST).content;
        results = json.loads(response);
        formattedResult = results["hello"];
        language = request.META['HTTP_ACCEPT_LANGUAGE']
        logging.info("TEST: " + pformat(formattedResult));
        print(results)
        template = jinja_env.get_template('templates/main.html')
        self.response.write(template.render({
            "results":formattedResult
        }))

class BookingHandler(webapp2.RequestHandler):
    def get(self):
        template = jinja_env.get_template('templates/booking.html')
        self.response.write(template.render())

class CurrencyExchangeHandler(webapp2.RequestHandler):
    def get(self):
        template = jinja_env.get_template('templates/currency.html')
        self.response.write(template.render())

class WeatherHandler(webapp2.RequestHandler):
    def get(self):
        template = jinja_env.get_template('templates/weather.html')
        self.response.write(template.render())

class TranslatorHandler(webapp2.RequestHandler):
    def get(self):
        template = jinja_env.get_template('templates/translator.html')
        self.response.write(template.render())

app = webapp2.WSGIApplication([
    ('/', MainPageHandler),
    ('/booking', BookingHandler),
    ('/currency-exchange', CurrencyExchangeHandler),
    ('/weather', WeatherHandler),
    ('/translate', TranslatorHandler),
    ], debug=True)
