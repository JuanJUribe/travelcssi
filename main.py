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

class SearchFormHandler(webapp2.RequestHandler):
    def get(self):
        template = jinja_env.get_template('templates/form.html')
        self.response.write(template.render())

class RecipeDisplayHandler(webapp2.RequestHandler):
    def post(self):
        ingredients = self.request.get('ingredients')
        recipe = self.request.get('recipe')
        base_url = 'http://www.recipepuppy.com/api/?'
        params = {
            'i':ingredients,
             'q':recipe
        }
        response = urlfetch.fetch(base_url+urlencode(params)).content
        results = json.loads(response)
        template = jinja_env.get_template('templates/recipe.html')
        self.response.write(template.render({
            'ingredients':ingredients,
            'recipe':recipe,
            'results':results,
        }))

app = webapp2.WSGIApplication([
    ('/', SearchFormHandler),
    ('/recipe', RecipeDisplayHandler)
    ], debug=True)
