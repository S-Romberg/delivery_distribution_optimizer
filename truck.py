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

  def __str__(self):
    return f'{self.id_}, {self.driver}, {self.packages}'

  # Assign packages based on matching zip codes
  def assign_packages(self, packages, recursive_call):
    zip_code = 0
    if self.packages and not recursive_call:
      zip_code = self.packages[0].zip_code
    else:
      for index in range(packages.size):
        package_id = index + 1
        package = packages.get(package_id)
        if package.assigned_truck is None:
          self.add_package(package)
          zip_code = package.zip_code
          package.assigned_truck = self
          break

    if zip_code != 0:
      for index in range(packages.size):
        package_id = index + 1
        package = packages.get(package_id)
        if package.assigned_truck is None and zip_code == package.zip_code and len(self.packages) < 16:
          self.add_package(package)
          package.assigned_truck = self
          break

      if len(self.packages) < 16:
        self.assign_packages(packages, True)

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
    if len(packages) == 1:
      return round(Truck.calculate_distance(self.current_location, package.location), 2)
    next_package = packages[1]
    distance = Truck.calculate_distance(self.current_location, package.location)
    distance_2 = Truck.calculate_distance(self.current_location, next_package.location)
    if distance_2 < distance:
      next_package.delivered_at = 'SOMETHING'
      self.packages.remove(next_package)
      self.delivered_packages.append(next_package)
      print('zip: ', next_package.zip_code)
      return round(distance_2, 2)
    else:
      package.delivered_at = 'SOMETHING'
      self.packages.remove(package)
      self.delivered_packages.append(package)
      print('zip: ', package.zip_code)
      return round(distance, 2)

  def deliver_packages(self):
    for i in range(len(self.packages)):
      distance = self.deliver_closest_package(self.packages)
      print('distance: ', distance)
      self.miles += distance


    # if len(packages) > 1:
    #   self.deliver_packages()
