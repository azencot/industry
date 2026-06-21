# Given an array nums of size n, return the majority element.

# The majority element is the element that appears more than ⌊n / 2⌋ 
# times. You may assume that the majority element always exists in the 
# array.
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res, count = nums[0], 1
        
        for num in nums[1:]:
            if res == num:
                count += 1
            else:
                count -= 1
                if count == 0:
                    res = num
                    count = 1

        return res

