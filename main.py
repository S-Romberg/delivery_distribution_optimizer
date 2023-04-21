import csv
from package import Package
from location import Location
from hash_map import HashMap


class Main:
    locations = HashMap(27)
    packages = HashMap(40)
    with open('data/Packages.csv', newline='', encoding='utf-8-sig') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        for index, row in enumerate(reader):
            packages.insert(int(row[0]), Package(*row))
    with open('data/Addresses and Hubs.csv', newline='', encoding='utf-8-sig') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        for index, row in enumerate(reader):
            id_ = index + 1
            locations.insert(id_, Location(id_, *row))
    with open('data/Distance.csv', newline='', encoding='utf-8-sig') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        # for index, row in enumerate(reader):
        # locations[index].set_distance(row)
