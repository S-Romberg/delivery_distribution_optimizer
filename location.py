class Location:
  def __init__(self, id_, name, address):
    self.id_ = id_
    self.name = name
    self.address = address
    self.distances = None

  def __str__(self):
    return f'{self.id_}, {self.name}, {self.address}, {self.distances}'
