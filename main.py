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

class FetchWeatherLocationHandler(webapp2.RequestHandler):
    def get(self, city_input):
        base_url = 'https://www.metaweather.com/api/location/search/?'
        params = {
            'query':city_input
        }
        response = urlfetch.fetch(base_url+urlencode(params)).content
        self.response.write(response)

class FetchWeatherHandler(webapp2.RequestHandler):
    def get(self, city_id):
        base_url = 'https://www.metaweather.com/api/location/'
        response = urlfetch.fetch(base_url+city_id).content
        self.response.write(response)

app = webapp2.WSGIApplication([
    ('/', MainPageHandler),
    ('/booking', BookingHandler),
    ('/currency-exchange', CurrencyExchangeHandler),
    ('/weather', WeatherHandler),
    ('/translate', TranslatorHandler),
    ('/fetchlocationweather/([\w %]*)', FetchWeatherLocationHandler),
    ('/fetchweather/(\d+)', FetchWeatherHandler),
    ], debug=True)
