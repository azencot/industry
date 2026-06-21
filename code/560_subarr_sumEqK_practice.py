# Given an array of integers nums and an integer k, return the total 
# number of subarrays whose sum equals to k.

# A subarray is a contiguous non-empty sequence of elements within an array.
class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        prefix_count = {0: 1}   # prefix sum 0 seen once
        curr_sum = 0
        count = 0

        for num in nums:
            curr_sum += num

            if curr_sum - k in prefix_count:
                count += prefix_count[curr_sum - k]

            prefix_count[curr_sum] = prefix_count.get(curr_sum, 0) + 1

        return count