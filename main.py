import webapp2
import jinja2
import os
import json
from google.appengine.api import urlfetch
from urllib import urlencode

jinja_env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

class MainPageHandler(webapp2.RequestHandler):
    def get(self):
        template = jinja_env.get_template('templates/main.html')
        self.response.write(template.render())

class BookingHandler(webapp2.RequestHandler):
    def get(self):
        template = jinja_env.get_template('templates/booking.html')
        self.response.write(template.render())
    # def post(self):
    #     ingredients = self.request.get('ingredients')
    #     recipe = self.request.get('recipe')
    #     base_url = 'http://www.recipepuppy.com/api/?'
    #     params = {
    #         'i':ingredients,
    #          'q':recipe
    #     }
    #     response = urlfetch.fetch(base_url+urlencode(params)).content
    #     results = json.loads(response)
    #     template = jinja_env.get_template('templates/recipe.html')
    #     self.response.write(template.render({
    #         'ingredients':ingredients,
    #         'recipe':recipe,
    #         'results':results,
    #     }))

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


app = webapp2.WSGIApplication([
    ('/', MainPageHandler),
    ('/booking', BookingHandler),
    ('/currency-exchange', CurrencyExchangeHandler),
    ('/weather', WeatherHandler),
    ('/translate', TranslatorHandler),
    ('/fetchweather/(\w+)', FetchWeatherLocationHandler),
    ], debug=True)
