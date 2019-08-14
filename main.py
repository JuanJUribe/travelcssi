import webapp2
import jinja2
import os
import json
from google.appengine.api import urlfetch
from google.appengine.api import users
from urllib import urlencode
import logging
from google.cloud import translate
from pprint import pformat

jinja_env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

class MainPageHandler(webapp2.RequestHandler):
    def get(self):
        login_url = None
        logout_url = None
        user =users.get_current_user()
        if user:
            logout_url = users.create_logout_url('/')
        else:
            login_url = users.create_login_url('/')
        base_url = "https://fourtonfish.com/hellosalut/?mode=auto";
        response = urlfetch.fetch(base_url, method=urlfetch.POST).content;
        results = json.loads(response);
        formattedResult = results["hello"];

        logging.info("TEST: " + pformat(formattedResult));
        template = jinja_env.get_template('templates/main.html')
        self.response.write(template.render({
            "results":results,
            'login_url':login_url,
            'logout_url':logout_url
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

class TranslatorHandler(webapp2.RequestHandler):
    def get(self):
        template = jinja_env.get_template('templates/translator.html')
        self.response.write(template.render())

class FetchTranslationHandler(webapp2.RequestHandler):
    def get(self, originalText, target):
        translate_client = translate.Client()

        translation = translate_client.translate(
            originalText,
            target_language=target)

        translation = json.dumps(translation)

        self.response.headers['Content-Type'] = 'application/json'
        self.response.write(translation)

class ContactHandler(webapp2.RequestHandler):
    def get(self):
        template = jinja_env.get_template('templates/contact.html')
        self.response.write(template.render())
    def post(self):
        print('big success')
        self.response.write('hola')

app = webapp2.WSGIApplication([
    ('/', MainPageHandler),
    ('/booking', BookingHandler),
    ('/currency-exchange', CurrencyExchangeHandler),
    ('/weather', WeatherHandler),
    ('/translate', TranslatorHandler),
    ('/fetchlocationweather/([\w %]*)', FetchWeatherLocationHandler),
    ('/fetchweather/(\d+)', FetchWeatherHandler),
    ('/fetchtranslate/([\w %]*)/(\w*)', FetchTranslationHandler),
    ('/contact-us', ContactHandler),
    ], debug=True)
