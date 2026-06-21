# Given an integer array nums and an integer k, return the k most frequent 
# elements. You may return the answer in any order.
import heapq

class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        uniques = {}

        # O(n) time and space, where n is the #num in nums
        for num in nums:
            if num in uniques:
                uniques[num] -= 1
            else:
                uniques[num] = -1

        # O(n log n) time, and O(n) space
        h = []
        for key in uniques:
            heapq.heappush(h, (uniques[key], key))

        # O(k log n) time, and O(k) space
        ret = []
        for _ in range(k):
            ret.append(heapq.heappop(h)[-1])

        return ret
