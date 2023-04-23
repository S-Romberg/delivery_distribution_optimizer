class Truck:
    def __init__(self, id_, depart_time):
        # print('Creating Package', id_, address, city, state, zip, deadline, weight, notes)
        self.id_ = id_
        self.depart_time = depart_time
        self.speed = 18
        self.driver = None
        self.packages = []

    def __str__(self):
        return f'{self.id_},'

    def total_distance(self, locations):
        for package in self.packages:
            for x in range(locations.size):
                id = x + 1
                location = locations.get(id)
                print(location.address, package.address)


    def add_package(self, package):
        self.packages.append(package)
