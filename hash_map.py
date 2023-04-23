# will use chaining for collisions
class HashMap:
    def __init__(self, size=20):
        self.size = size
        self.list = [] * size
        for x in range(size):
            self.list.append([])

    def insert(self, key, item):
        # print('Inserting', item)
        # print('bucket address', hash(key) % len(self.list))
        bucket = hash(key) % len(self.list)
        # print('Index currently holds:', self.list[bucket])
        self.list[bucket] = item

    def get(self, key):
        bucket = hash(key) % len(self.list)
        # print('getting', self.list[bucket], bucket)
        return self.list[bucket]

    def remove(self, key):
        print("REMOVING: ", key)
        bucket = hash(key) % len(self.list)
        self.list[bucket] = None
