from google.appengine.ext import ndb

class User(ndb.Model):
    email = ndb.StringProperty(required=True)
    first_name = ndb.StringProperty(required=True)
    last_name = ndb.StringProperty(required=True)
    language = ndb.StringProperty(required=True)
    country = ndb.StringProperty(required=True)
    city = ndb.StringProperty(required=True)
    currency = ndb.StringProperty(required=True)
