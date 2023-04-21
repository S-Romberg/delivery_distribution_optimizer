class Location:
    def __init__(self, name, address):
        self.name = name
        self.address = address

    def set_distance(self, distance):
        self.distances = distance

    def __str__(self):
        return self.name, self.address, self.distances
