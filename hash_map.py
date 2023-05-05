class HashMap:
  def __init__(self, size=20):
    self.size = size
    self.list = [] * size
    for x in range(size):
      self.list.append([])

  def insert(self, key, item):
    bucket = hash(key) % len(self.list)
    self.list[bucket] = item

  def get(self, key):
    bucket = hash(key) % len(self.list)
    return self.list[bucket]

  def remove(self, key):
    bucket = hash(key) % len(self.list)
    self.list[bucket] = None
