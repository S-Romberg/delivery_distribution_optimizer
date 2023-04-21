# create a hash table with an init function
# each item in the hash table is called a bucket
# the insert function will insert an item into the hash table by hashing the item and inserting it into the bucket
# will use chaining for collisions
class HashMap:
    def __init__(self, size=20):
        self.size = size
        self.list = [] * size
        for x in range(size):
            self.list.append([])
        print(self.list)

    def insert(self, item):
        key = hash(item) % self.size
        self.list[key] = item

    def get(self, key):
        return self.list[key]
