# Given an integer array nums and an integer k, return true if there are two distinct 
# indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.
class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        seen = {}

        for i, num in enumerate(nums):
            if num in seen and i - seen[num] <= k:
                    return True
            seen[num] = i

        return False