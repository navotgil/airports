import webapp2
import jinja2
import os
from webapp2_extras import routes


import utils


J_E = jinja2.Environment(loader=jinja2.FileSystemLoader(os.path.dirname(__file__)))

class MainHandler(webapp2.RequestHandler):
    def get(self):
        template = J_E.get_template('/html/index.html')
        self.response.write(template.render({"version":"001"}))

class CreateDB(webapp2.RequestHandler):
    def get(self):
        counter = utils.createDbFromCSV('large_airports.csv')
        self.response.write("Added " + str(counter) + " airports")

class Airports(webapp2.RequestHandler):
    def get(self):
        template = J_E.get_template('/html/airports.html')
        airports = utils.db.getAllAirports()
        contex = {}
        contex["airports"] = airports
        self.response.write(template.render(contex))

class AirportPage(webapp2.RequestHandler):
    def get(self, ident):
        template = J_E.get_template('/html/airport.html')
        airport = utils.db.getAirport(ident)
        contex = {}
        contex["airport"] = airport
        self.response.write(template.render(contex))

app = webapp2.WSGIApplication([
    routes.RedirectRoute('/', handler=MainHandler, name='main', strict_slash=True),
    routes.RedirectRoute('/airports', handler=Airports, name='airports', strict_slash=True),
    routes.RedirectRoute('/airports/<ident>', handler=AirportPage, name='airport', strict_slash=True),
    routes.RedirectRoute('/create_db', handler=CreateDB, name='create_db', strict_slash=True)
], debug=True)
