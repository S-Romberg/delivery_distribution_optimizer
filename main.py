import csv
from datetime import datetime
from datetime import timedelta

from package import Package
from location import Location
from hash_map import HashMap
from truck import Truck


class Main:
  def __init__(self):
    self.locations = HashMap(27)
    self.packages = HashMap(40)
    self.sorted_packages = []
    self.starting_location = None
    self.truck_1 = Truck(1, timedelta(hours=8))
    self.truck_2 = Truck(2, timedelta(hours=9, minutes=5))
    self.truck_3 = Truck(3, timedelta(hours=10, minutes=20))
    self.mile_count = 0.0
    self.time_saved = 0.0

  def find_location(self, address):
    for index in range(self.locations.size):
      location = self.locations.get(index)
      if address in location.name or address in location.address:
        return location
    return None

  def deliver_packages(self, truck):
    truck.deliver_packages()
    self.mile_count += truck.miles

  def run(self):
    # Read all CSV files and populate data structures
    with open('data/Packages.csv', newline='', encoding='utf-8-sig') as csvfile:
      reader = csv.reader(csvfile, delimiter=',')
      for index, row in enumerate(reader):
        self.sorted_packages.append(row)
    with open('data/Addresses and Hubs.csv', newline='', encoding='utf-8-sig') as csvfile:
      reader = csv.reader(csvfile, delimiter=',')
      for index, row in enumerate(reader):
        id_ = index + 1
        self.locations.insert(id_, Location(id_, *row))
        if id_ == 1:
          self.starting_location = self.locations.get(id_)
    with open('data/Distance.csv', newline='', encoding='utf-8-sig') as csvfile:
      reader = csv.reader(csvfile, delimiter=',')
      for index, row in enumerate(reader):
        self.locations.get(index + 1).set_distance(row)

    # Sort packages by address
    self.sorted_packages = sorted(self.sorted_packages, key=lambda x: x[4])
    for package in self.sorted_packages:
      self.packages.insert(int(package[0]), Package(*package))

    # Loop through all packages, finding each by id and adding it to a truck
    for index in range(self.packages.size):
      package_id = index + 1
      package = self.packages.get(package_id)
      package.location = self.find_location(package.address)
      if package.notes is not None and package.assigned_truck is None:
        # All late packages will go on truck 2
        if package.notes == 'Delayed on flight---will not arrive to depot until 9:05 am' or package.notes == 'Can only be on truck 2':  # All early packages will go on one truck that will leave at 8am
          self.truck_2.add_package(package)
          package.assigned_truck = self.truck_2
        # All incorrect address packages will go on truck 3
        elif package.notes == 'Wrong address listed':
          self.truck_3.add_package(package)
          package.assigned_truck = self.truck_3
        # All packages that need to be delivered together will go on truck 1
        elif "Must be delivered with " in package.notes:
          self.truck_1.add_package(package)
          package.assigned_truck = self.truck_1
        # All other packages that need to be delivered early will go on truck 1
        elif package.deadline != 'EOD':
          self.truck_1.add_package(package)
          package.assigned_truck = self.truck_1

    # Set starting location for trucks and assign the rest of the packages
    self.truck_1.current_location = self.starting_location
    self.truck_2.current_location = self.starting_location
    self.truck_3.current_location = self.starting_location
    self.truck_3.assign_packages(self.packages)
    self.truck_2.assign_packages(self.packages)
    self.truck_1.assign_packages(self.packages)

    print('TRUCK 1')
    self.deliver_packages(self.truck_1)
    print(self.mile_count)
    print('TRUCK 2')
    self.deliver_packages(self.truck_2)
    print(self.mile_count)
    print('TRUCK 3')
    self.deliver_packages(self.truck_3)
    print(self.mile_count)

    @staticmethod
    def unassigned_packages(packages):
      count = 0
      assigned = 0
      for index in range(packages.size):
        package_id = index + 1
        package = packages.get(package_id)
        if package.assigned_truck is None:
          count += 1
        else:
          assigned += 1
      return count

#  print('unassigned', unassigned_packages(packages))

if __name__ == "__main__":
  main = Main()
  main.run()