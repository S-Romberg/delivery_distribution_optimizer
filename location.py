class Location:
    def __init__(self, id, name, address):
        print('Creating Location', id, name, address)
        self.id = id
        self.name = name
        self.address = address
        self.distances = None

    def set_distance(self, distance):
        self.distances = distance

    def __str__(self):
        return self.id, self.name, self.address, self.distances
