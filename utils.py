import csv
import json
import db


def createDbFromCSV(filename):
    counter = 0
    with open(filename) as csvfile:
        reader = csv.DictReader(csvfile)
        added = False
        for row in reader:
            for cell in row:
                row[cell] = row[cell].decode('utf-8')
            added = db.addAirport(row)
            if added:
                counter = added + 1
    return counter