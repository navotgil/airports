from google.appengine.ext import ndb


class Airport(ndb.Model):
  ident = ndb.StringProperty()
  name = ndb.StringProperty()
  latitude_deg = ndb.StringProperty()
  longitude_deg = ndb.StringProperty()
  iso_country = ndb.StringProperty()
  home_link = ndb.StringProperty()
  wikipedia_link = ndb.StringProperty()