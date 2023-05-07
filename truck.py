from datetime import timedelta
class Truck:
  def __init__(self, id_, depart_time):
    # print('Creating Package', id_, address, city, state, zip, deadline, weight, notes)
    self.id_ = id_
    self.depart_time = depart_time
    self.speed = 18
    self.driver = None
    self.packages = []
    self.delivered_packages = []
    self.current_location = None
    self.miles = 0.0
    self.test_location = None
    self.current_time = depart_time

  def __str__(self):
    return f'{self.id_}, {self.driver}, {self.packages}'

  # Assign packages based on matching zip codes
  def assign_packages(self, packages):
    for index in range(packages.size):
      if len(self.packages) < 16:
        package = packages.get(index + 1)
        if package.assigned_truck is None:
          package.assigned_truck = self
          self.packages.append(package)

  def add_package(self, package):
    self.packages.append(package)

  @staticmethod
  def calculate_distance(location_1, location_2):
    try:
      if location_1.id_ > location_2.id_:
        return float(location_1.distances[location_2.id_ - 1])
      elif location_2.id_ > location_1.id_:
        return float(location_2.distances[location_1.id_ - 1])
      else:
        return 0.0
    except Exception as e:
      print(e)
      return 0.0

  def deliver_closest_package(self, packages):
    package = packages[0]
    distance_3 = 1000

    if len(packages) == 1:
      self.packages.remove(package)
      self.delivered_packages.append(package)
      return round(Truck.calculate_distance(self.current_location, package.location), 2)
    if len(packages) > 2:
      package_2 = packages[2]
      distance_3 = Truck.calculate_distance(self.current_location, package_2.location)

    package_1 = packages[1]
    distance = Truck.calculate_distance(self.current_location, package.location)
    distance_2 = Truck.calculate_distance(self.current_location, package_1.location)

    if distance_2 < distance and distance_2 < distance_3:
      if package_1 in self.delivered_packages:
        return

      self.current_time = self.current_time + timedelta(hours=(round(distance_2, 2) / self.speed))
      package.delivered_at = self.current_time
      self.current_location = package_1.location
      self.packages.remove(package_1)
      self.delivered_packages.append(package_1)
      return round(distance_2, 2)
    elif distance_3 < distance and distance_3 < distance_2:
      if package_2 in self.delivered_packages:
        return
      self.current_time = self.current_time + timedelta(hours=(round(distance_3, 2) / self.speed))
      print(self.current_time)
      package.delivered_at = self.current_time
      self.current_location = package_2.location
      self.packages.remove(package_2)
      self.delivered_packages.append(package_2)
      # print('zip: ', package_2.zip_code)
      return round(distance_3, 2)
    else:
      if package in self.delivered_packages:
        return
      self.current_time = self.current_time + timedelta(hours=(round(distance, 2) / self.speed))
      package.delivered_at = self.current_time
      self.current_location = package.location
      self.packages.remove(package)
      self.delivered_packages.append(package)
      # print('zip: ', package.zip_code)
      return round(distance, 2)

  def deliver_packages(self):
    for i in range(len(self.packages)):
      distance = self.deliver_closest_package(self.packages)
      self.miles += distance


