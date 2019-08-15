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
from HTMLParser import HTMLParser
import time

from models import User

jinja_env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

class MainPageHandler(webapp2.RequestHandler):
    def get(self):
        template = jinja_env.get_template('templates/main.html')
        login_url = None
        logout_url = None
        user = users.get_current_user()
        base_url = "https://fourtonfish.com/hellosalut/?";
        time.sleep(1)
        if user:
            try:
                language = User.query().filter(User.email == user.email()).get().language
            except:
                language = 'en'
            params={
                'cc':language
            }
            response = urlfetch.fetch(base_url+urlencode(params), method=urlfetch.POST).content;
            results = json.loads(response);
            formattedResult = results["hello"];
            logging.info("TEST: " + pformat(formattedResult));
            logout_url = users.create_logout_url('/')
            h = HTMLParser()
            unescapedResult = h.unescape(formattedResult)
            self.response.write(template.render({
                'results':unescapedResult,
                'login_url':login_url,
                'logout_url':logout_url
            }))
        else:
            login_url = users.create_login_url('/check-user')
            template = jinja_env.get_template('templates/main.html')
            self.response.write(template.render({
                'login_url':login_url,
                'logout_url':logout_url
            }))

class CheckUserHandler(webapp2.RequestHandler):
    def get(self):
        google_user = users.get_current_user()
        if google_user:
            user = User.query().filter(User.email == google_user.email()).get()
            if user:
                return self.redirect('/')
            else:
                return self.redirect('/profile')
        else:
            return self.redirect('/')

class ProfileHandler(webapp2.RequestHandler):
    def get(self):
        template = jinja_env.get_template('templates/get-profile.html')
        self.response.write(template.render())
    def post(self):
        first_name = self.request.get('first_name')
        last_name = self.request.get('last_name')
        country = self.request.get('country')
        countryName = country.split(':')[0]
        language = 'en'
        try:
            language = country.split(':')[1]
        except:
            pass
        city = self.request.get('city')
        currency = self.request.get('currency')
        if users.get_current_user() is None:
            time.sleep(1)
        email = users.get_current_user().email()

        User(city=city, currency=currency, language=language, email=email, first_name=first_name, last_name=last_name, country=countryName).put()

        return self.redirect('/')

class BookingHandler(webapp2.RequestHandler):
    def get(self):
        template = jinja_env.get_template('templates/booking.html')
        self.response.write(template.render())

class CurrencyExchangeHandler(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()
        time.sleep(1)
        if user:
            try:
                currency = User.query().filter(User.email == user.email()).get().currency
                template = jinja_env.get_template('templates/currency.html')
                self.response.write(template.render({
                    'currency':currency
                }))
            except:
                template = jinja_env.get_template('templates/currency.html')
                self.response.write(template.render())
        else:
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
        user = users.get_current_user()
        time.sleep(1)
        if user:
            try:
                lang = User.query().filter(User.email == user.email()).get().language
                auto_lang = 'Predetermined - '+lang.upper()
                template = jinja_env.get_template('templates/translator.html')
                self.response.write(template.render({
                    'autoLang':auto_lang
                }))
            except:
                template = jinja_env.get_template('templates/translator.html')
                self.response.write(template.render())
        else:
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

class FetchCountryHandler(webapp2.RequestHandler):
    def get(self):
        base_url = 'http://countryapi.gear.host/v1/Country/getCountries'
        response = urlfetch.fetch(base_url).content
        self.response.write(response)

class ContactHandler(webapp2.RequestHandler):
    def get(self):
        google_user = users.get_current_user()
        user = User.query().filter(User.email == google_user.email()).get()
        if user:
            template = jinja_env.get_template('templates/contact.html')
            self.response.write(template.render({
                'firstName':user.first_name,
                'lastName':user.last_name,
                'country':user.country,
                'email':user.email,
            }))
        else:
            return self.redirect('/profile')

app = webapp2.WSGIApplication([
    ('/', MainPageHandler),
    ('/check-user', CheckUserHandler),
    ('/profile', ProfileHandler),
    ('/booking', BookingHandler),
    ('/currency-exchange', CurrencyExchangeHandler),
    ('/weather', WeatherHandler),
    ('/translate', TranslatorHandler),
    ('/fetchlocationweather/([\w %]*)', FetchWeatherLocationHandler),
    ('/fetchweather/(\d+)', FetchWeatherHandler),
    ('/fetchtranslate/([\w %]*)/(\w*)', FetchTranslationHandler),
    ('/fetchcountry', FetchCountryHandler),
    ('/contact-us', ContactHandler),
    ], debug=True)
