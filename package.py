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

  def status(self):
    if self.delivered_at is None and self.assigned_truck.depart_time < self.assigned_truck.current_time:
      return 'En route'
    elif self.delivered_at is not None:
      return 'Delivered'
    else:
      return 'At the hub'

  def status_by_time(self, start_time, end_time):
    if self.delivered_at <= end_time:
      return 'Delivered'
    elif self.assigned_truck.depart_time >= start_time:
      return 'At the hub'
    elif self.delivered_at >= end_time and start_time > self.assigned_truck.depart_time:
      return 'In transit'


  def __str__(self):
    return f'id: {self.id_}, address: {self.address}, city: {self.city}, state: {self.state}, zip code: {self.zip_code}, deadline: {self.deadline}, weight: {self.weight}, notes: {self.notes}, delivered_at: {self.delivered_at}'
    # return f' delivered_at: {self.delivered_at}'
