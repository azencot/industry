import heapq

class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.cache = {}
        self.heap = []
        self.access = 0


    def get(self, key):
        """
        :type key: int
        :rtype: int
        """


    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if key not in self.cache:
            self.cache[key] = value
            self.heap.heappush([self.access, key])

        

        self.access += 1

        # cache exceeds capacity
        if len(self.heap) > self.capacity:
            key = self.heap.heappop()
            self.cache.pop(key)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)