class HashMap:

    def __init__(self):
        self.capacity = 10
        self.buckets = [[] for _ in range(self.capacity)]
        self.count = 0

    def hash(self, key):
        return key % self.capacity

    def put(self, key, value):
        idx = self.hash(key)
        bucket = self.buckets[idx]
        for pair in bucket:
            if pair[0] == key:
                pair[1] = value
                return
        bucket.append([key, value])
        self.count += 1

    def get(self, key):
        idx = self.hash(key)
        for pair in self.buckets[idx]:
            if pair[0] == key:
                return pair[1]
        return -1

    def containsKey(self, key):
        idx = self.hash(key)
        for pair in self.buckets[idx]:
            if pair[0] == key:
                return True
        return False

    def remove(self, key):
        idx = self.hash(key)
        bucket = self.buckets[idx]
        for i in range(len(bucket)):
            if bucket[i][0] == key:
                bucket.pop(i)
                self.count -= 1
                return

    def size(self):
        return self.count
