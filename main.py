import csv
from package import Package
from location import Location

class Main:
    locations = []
    packages = []
    with open('data/Packages.csv', newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        for index, row in enumerate(reader):
            packages.append(Package(*row))
    with open('data/Addresses and Hubs.csv', newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        for index, row in enumerate(reader):
            locations.append(Location(*row))
    with open('data/Distance.csv', newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        for index, row in enumerate(reader):
            locations[index].set_distance(row)