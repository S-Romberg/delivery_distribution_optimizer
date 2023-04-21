class Package:
    def __init__(self, id_, address, city, state, zip, deadline, weight, notes):
        # print('Creating Package', id_, address, city, state, zip, deadline, weight, notes)
        self.id_ = id_
        self.address = address
        self.city = city
        self.state = state
        self.zip = zip
        self.deadline = deadline
        self.weight = weight
        self.notes = notes

    def __str__(self):
        return f'{self.id_}, {self.address}, {self.city}, {self.state}, {self.zip}, {self.deadline}, {self.weight}, {self.notes}'
