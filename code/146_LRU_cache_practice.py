# Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.

# Implement the LRUCache class:

# LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
# int get(int key) Return the value of the key if the key exists, otherwise return -1.
# void put(int key, int value) Update the value of the key if the key exists. 
# Otherwise, add the key-value pair to the cache. If the number of keys exceeds the 
# capacity from this operation, evict the least recently used key.
# The functions get and put must each run in O(1) average time complexity.
class Node:
    def __init__(self, key, val, prev, next):
        self.key = key
        self.val = val
        self.prev = prev
        self.next = next

class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity

        self.start = Node(-1,-1, None, None)
        self.end = Node(-2,-1, self.start, None)
        self.start.next = self.end

        self.cache = {}

    def removeNode(self, node):
        prev = node.prev
        next = node.next

        prev.next = next
        next.prev = prev

    def addNodeToEnd(self, node):
        prev = self.end.prev

        prev.next = node
        node.prev = prev

        node.next = self.end
        self.end.prev = node

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.cache:
            node = self.cache[key]
            
            self.removeNode(node)
            self.addNodeToEnd(node)
            return node.val

        return -1

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if key in self.cache:
            node = self.cache[key]
            node.val = value

            self.removeNode(node)
            self.addNodeToEnd(node)

        else:
            self.cache[key] = Node(key, value, self.end.prev, self.end)
            self.addNodeToEnd(self.cache[key])

        # remove LRU
        if len(self.cache) > self.capacity:
            node = self.start.next
            self.removeNode(node)
            del self.cache[node.key]


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)