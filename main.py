import csv
from package import Package
from location import Location
from hash_map import HashMap

class Main:
    locations = HashMap(27)
    packages = HashMap(40)
    with open('data/Packages.csv', newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        for index, row in enumerate(reader):
            packages.insert(Package(*row))
    with open('data/Addresses and Hubs.csv', newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        for index, row in enumerate(reader):
            locations.insert(Location(index + 1, *row))
    with open('data/Distance.csv', newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        # for index, row in enumerate(reader):
            # locations[index].set_distance(row)
