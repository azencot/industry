# Given an integer array nums with possible duplicates, randomly output 
# the index of a given target number. You can assume that the given target 
# number must exist in the array.

# Implement the Solution class:

# Solution(int[] nums) Initializes the object with the array nums.

# int pick(int target) Picks a random index i from nums where 
# nums[i] == target. If there are multiple valid i's, then each index 
# should have an equal probability of returning.

# sounds like a simple dictionary
import random

class Solution(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """

        self.nums_dict = {}     # hash table for indices

        # O(n) time, O(n) memory
        for i, num in enumerate(nums):
            if num not in self.nums_dict:
                self.nums_dict[num] = [i]
            else:
                self.nums_dict[num].append(i)

    def pick(self, target):
        """
        :type target: int
        :rtype: int
        """
        return random.choice(self.nums_dict[target])

        # # reservoir sampling
        # count, res = 0, -1
        # for i, num in enumerate(self.nums):
        #     if num == target:
        #         count += 1
            
        #         if random.random() < 1.0 / count:
        #             res = i

        # return res



