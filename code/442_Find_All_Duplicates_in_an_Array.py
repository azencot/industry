# Given an integer array nums of length n where all the integers of nums 
# are in the range [1, n] and each integer appears at most twice, return 
# an array of all the integers that appears twice.

# You must write an algorithm that runs in O(n) time and uses only 
# constant auxiliary space, excluding the space needed to store the output
class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        dup = []
        for num in nums:
            
            if nums[abs(num) - 1] > 0:
                nums[abs(num) - 1] *= -1
            else:
                dup.append(- nums[abs(num) - 1])

        return dup


sol = Solution()
sol.findDuplicates([4,3,2,7,8,2,3,1])



