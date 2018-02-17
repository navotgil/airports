import models
import logging


def getAirport(ident):
    return models.Airport.query(models.Airport.ident == ident).get()

def getAllAirports():
    return models.Airport.query().order(models.Airport.name)


def addAirport(airportJson):
    if "ident" in airportJson and not getAirport(airportJson["ident"]):
        entry = models.Airport()
        for prop in airportJson:
            if hasattr(entry,prop):
                setattr(entry, prop, airportJson[prop])
        entry.put()
        return True
    return False