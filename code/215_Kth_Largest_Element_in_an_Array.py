# Given an integer array nums and an integer k, return the kth largest 
# element in the array.

# Note that it is the kth largest element in the sorted order, not the kth 
# distinct element.

# Can you solve it without sorting?
# import heapq
import random

class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # h = []

        # for num in nums:
        #     heapq.heappush(h, num)

        #     if len(h) > k:
        #         heapq.heappop(h)

        # return h[0]

        # finding the kth largest element is the same as finding len(nums) - k smallest element
        # can use quickselect: O(n) on average
        target = len(nums) - k
        left, right = 0, len(nums) - 1

        def partition(left, right):
            # pivot = nums[right]
            pivot = nums[random.randint(left, right)]
            store = left

            for i in range(left, right):
                if nums[i] < pivot:
                    nums[store], nums[i] = nums[i], nums[store]
                    store += 1

            nums[store], nums[right] = nums[right], nums[store]
            return store

        while left <= right:
            pivot_index = partition(left, right)
            if pivot_index == target:
                return nums[pivot_index]
            elif target < pivot_index:
                right = pivot_index - 1
            else:
                left = pivot_index + 1


        target = len(nums) - k
        left, right = 0, len(nums) - 1

        def partition(left, right):
            pivot = nums[right]
            store = left

            for i in range(left, right):
                if nums[i] < pivot:
                    nums[store], nums[i] = nums[i], nums[store]
                    store += 1

            nums[store], nums[right] = nums[right], nums[store]
            return store

        while left <= right:
            pivot_index = partition(left, right)

            if pivot_index == target:
                return nums[pivot_index]
            elif pivot_index < target:
                right = pivot_index - 1
            else:
                left = pivot_index + 1