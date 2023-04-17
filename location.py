class Location:
    def __init__(self, name, address):
        print('Creating Location', name, address)
        self.name = name
        self.address = address

    def set_distance(self, distance):
        print('setting distance', distance)
        self.distances = distance