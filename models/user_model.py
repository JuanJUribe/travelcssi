from google.appengine.ext import ndb

class User(ndb.Model):
    google_auth_key = ndb.KeyProperty(required=True)
    first_name = ndb.StringProperty(required=True)
    last_name = ndb.StringProperty(required=True)
    age = ndb.IntegerProperty(required=True)
    lenguage = ndb.StringProperty(required=True)
    country = ndb.StringProperty(required=True)
    city_name = ndb.StringProperty(required=True)
    currency = ndb.StringProperty(required=True)
