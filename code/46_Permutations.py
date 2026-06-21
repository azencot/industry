# Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.

class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums:
            return [[]]

        res = []
        for i, num in enumerate(nums):
            for perm in self.permute(nums[:i] + nums[i+1:]):
                res.append([num] + perm)

        return res

     
sol = Solution()
print(sol.permute([5,4,6,2]))