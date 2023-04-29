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
  for index in range(packages.size):
    package_id = index + 1
    package = packages.get(package_id)
    if package.notes is not None and package.assigned_truck is None:
      # All late packages will go on truck 2
      if package.notes == 'Delayed on flight---will not arrive to depot until 9:05 am' or package.notes == 'Can only be on truck 2':  # All early packages will go on one truck that will leave at 8am
        truck_2.add_package(package)
        package.assigned_truck = truck_2
      # All incorrect address packages will go on truck 3
      elif package.notes == 'Wrong address listed':
        truck_3.add_package(package)
        package.assigned_truck = truck_3
      # All packages that need to be delivered together will go on truck 1
      elif "Must be delivered with " in package.notes:
        truck_1.add_package(package)
        package.assigned_truck = truck_1
      # All other packages that need to be delivered early will go on truck 1
      elif package.deadline != 'EOD':
        truck_1.add_package(package)
        package.assigned_truck = truck_1

  truck_1.assign_packages(packages, False)
  truck_2.assign_packages(packages, False)
  truck_3.assign_packages(packages, False)
  print('truck 1 packages', len(truck_1.packages))
  print('truck 2 packages', len(truck_2.packages))
  print('truck 3 packages', len(truck_3.packages))

  # next we need to assign drivers to the trucks, there are only 2 drivers
  # driver 1 will drive truck 1 and 3, in that order
  # driver 2 will drive truck 2

  # Then we need to loop through the trucks and deliver the packages.
  # We need to count the miles between where we are and where the package is going and add that to the mileage counter
  #     - In order to count the miles we need to be able to compare the addresses to the locations data
  #     - We need to have the location ID for the current address and the destination address
  #     - After we find the address in the location data we need to take that ID and use it to find the distance in the distance data, which is just a two dimensaional array so it should be [location id 1][location id 2]
  # then we need to divide the miles by 18 and add that time to the hour counter and save it as the delivery time for the package

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

  print('unassigned', unassigned_packages(packages))
