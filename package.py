class Package:
  def __init__(self, id_, address, city, state, zip_code, deadline, weight, notes):
    # print('Creating Package', id_, address, city, state, zip_code, deadline, weight, notes)
    self.id_ = id_
    self.address = address
    self.city = city
    self.state = state
    self.zip_code = zip_code
    self.deadline = deadline
    self.weight = weight
    self.notes = notes
    self.delivered_at = None
    self.assigned_truck = None
    self.location = None
    self.status = 'At Hub'

  def set_delivered_at(self, time):
    self.delivered_at = time

  def __str__(self):
    return f'delivered_at: {self.delivered_at}. {self.id_}, {self.address}, {self.city}, {self.state}, {self.zip_code}, {self.deadline}, {self.weight}, {self.notes}'
