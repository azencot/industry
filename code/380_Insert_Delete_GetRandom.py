# Implement the RandomizedSet class:

# RandomizedSet() Initializes the RandomizedSet object.

# bool insert(int val) Inserts an item val into the set if not present. 
# Returns true if the item was not present, false otherwise.

# bool remove(int val) Removes an item val from the set if present. 
# Returns true if the item was present, false otherwise.

# int getRandom() Returns a random element from the current set of 
# elements (it's guaranteed that at least one element exists when this 
# method is called). Each element must have the same probability of being 
# returned.

# You must implement the functions of the class such that each function 
# works in average O(1) time complexity.
class RandomizedSet(object):

    def __init__(self):
        self.vals_dict = {}     # used for O(1) insert/remove
        self.vals_list = []     # used for O(1) getRandom

    def insert(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if val not in self.vals_dict:
            self.vals_dict[val] = len(self.vals_list)
            self.vals_list.append(val)
            return True
        else:
            return False

    def remove(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if val in self.vals_dict:
            idx = self.vals_dict[val]

            val2 = self.vals_list[-1]

            self.vals_list[idx] = val2
            self.vals_dict[val2] = idx

            self.vals_list.pop()
            del self.vals_dict[val]

            return True
        else:
            return False

    def getRandom(self):
        """
        :rtype: int
        """
        import random

        idx = random.randint(0, len(self.vals_list) - 1)
        return self.vals_list[idx]
