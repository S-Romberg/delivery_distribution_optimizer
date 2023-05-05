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
    self.truck_1 = Truck(1, timedelta(hours=8))
    self.truck_2 = Truck(2, timedelta(hours=9, minutes=5))
    self.truck_3 = Truck(3, timedelta(hours=10, minutes=20))
    self.mile_count = 0.0

  def find_location(self, address):
    for index in range(self.locations.size):
      location = self.locations.get(index)
      if address in location.address:
        return location
    return None

  # Next steps:
  #   Mark packages as delivered after adding delivery miles
  #   Only work with undelivered packages (this will require a decent amount of code at the beginning of the for loop)
  #   Grab next two packages and deliver to the closer one
  def deliver_packages(self, truck):
    current_location = None
    for i in range(0, len(truck.packages)):
      package = truck.packages[i]
      try:
        next_package = truck.packages[i + 1]
      except IndexError:
        print('error')
      if current_location is None:
        current_location = self.find_location(package.address)
      else:
        next_location = self.find_location(package.address)
        next_location_2 = self.find_location(next_package.address)
        if (next_location is None):
          print('could not find address', package.address)
        distance = Truck.calculate_distance(current_location, next_location)
        distance_2 = Truck.calculate_distance(current_location, next_location_2)
        if(distance_2 < distance):
          print('smaller by: ', distance - distance_2)
        self.mile_count += distance

  def run(self):

    with open('data/Packages.csv', newline='', encoding='utf-8-sig') as csvfile:
      reader = csv.reader(csvfile, delimiter=',')
      for index, row in enumerate(reader):
        self.packages.insert(int(row[0]), Package(*row))
    with open('data/Addresses and Hubs.csv', newline='', encoding='utf-8-sig') as csvfile:
      reader = csv.reader(csvfile, delimiter=',')
      for index, row in enumerate(reader):
        id_ = index + 1
        self.locations.insert(id_, Location(id_, *row))
    with open('data/Distance.csv', newline='', encoding='utf-8-sig') as csvfile:
      reader = csv.reader(csvfile, delimiter=',')
      for index, row in enumerate(reader):
        self.locations.get(index + 1).set_distance(row)

    # Loop through all packages, finding each by id and adding it to a truck
    for index in range(self.packages.size):
      package_id = index + 1
      package = self.packages.get(package_id)
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

    self.truck_1.assign_packages(self.packages, False)
    self.truck_2.assign_packages(self.packages, False)
    self.truck_3.assign_packages(self.packages, False)

    # next we need to assign drivers to the trucks, there are only 2 drivers
    # driver 1 will drive truck 1 and 3, in that order
    # driver 2 will drive truck 2

    # Then we need to loop through the trucks and deliver the packages.
    # We need to count the miles between where we are and where the package is going and add
    # that to the mileage counter
    #     - In order to count the miles we need to be able to compare the addresses to
    #       the locations data
    #     - We need to have the location ID for the current address and the destination address
    #     - After we find the address in the location data we need to take that ID and use it
    #       to find the distance in the distance data, which is just a two dimensaional array
    #       so it should be [location id 1][location id 2]
    # then we need to divide the miles by 18 and add that time to the hour counter
    # and save it as the delivery time for the package


    # How do we find the two locations in the location data?
    # Once we have them we can use the ids, but we need to find them based off of the address.

      # truck.location = location_2
      # package.delivery_time = truck.departure_time + timedelta(hours=mile_count / 18)

    self.deliver_packages(self.truck_1)
    print(self.mile_count)
    self.deliver_packages(self.truck_2)
    print(self.mile_count)
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