class HashMap:
  def __init__(self, size=20):
    self.size = size
    self.list = [] * size
    for x in range(size):
      self.list.append([])

  # Insert an item into the hash map
  def insert(self, key, item):
    bucket = hash(key) % len(self.list)
    self.list[bucket] = item

  # Retrieve an item from the hash map
  def get(self, key):
    bucket = hash(key) % len(self.list)
    return self.list[bucket]

  # Remove an item from the hash map
  def remove(self, key):
    bucket = hash(key) % len(self.list)
    self.list[bucket] = None
