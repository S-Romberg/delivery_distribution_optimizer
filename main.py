import csv
from datetime import datetime
from datetime import timedelta

from package import Package
from location import Location
from hash_map import HashMap
from truck import Truck


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
    for index, row in enumerate(reader):
      locations.get(index + 1).set_distance(row)

  truck_1 = Truck(1, timedelta(hours=8))
  truck_2 = Truck(2, timedelta(hours=9, minutes=5))
  truck_3 = Truck(3, timedelta(hours=10, minutes=20))

  # Loop through all packages, finding each by id and adding it to a truck
  print('packages size: ', packages.size)
  for index in range(packages.size):
    package_id = index + 1
    package = packages.get(package_id)
    if package.notes is not None and package.assigned_truck is None:
      if package.notes == 'Delayed on flight---will not arrive to depot until 9:05 am' or package.notes == 'Can only be on truck 2':                # All early packages will go on one truck that will leave at 8am
        truck_2.add_package(package)
        package.assigned_truck = truck_2
      elif package.notes == 'Wrong address listed':
        truck_3.add_package(package)
        package.assigned_truck = truck_3
    elif package.assigned_truck is None:
      truck_1.add_package(package)

  print(len(truck_1.packages))
  print(len(truck_2.packages))
  print(len(truck_3.packages))
  print(truck_3.total_distance(locations))
  def calculate_distance(self, first_address, second_address):
    print(first_address, second_address)
