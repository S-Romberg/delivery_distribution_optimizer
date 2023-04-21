class Package:
    def __init__(self, id, address, city, state, zip, deadline, weight, notes):
        print('Creating Package', id, address, city, state, zip, deadline, weight, notes)
        self.id = id
        self.address = address
        self.city = city
        self.state = state
        self.zip = zip
        self.deadline = deadline
        self.weight = weight
        self.notes = notes

    def __str__(self):
        return self.id, self.address, self.city, self.state, self.zip, self.deadline, self.weight, self.notes
