# There is an integer array nums sorted in ascending order (with distinct values).

# Prior to being passed to your function, nums is possibly left rotated at an unknown index k (1 <= k < nums.length) such that the resulting array 
# is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be left rotated by 3 indices 
# and become [4,5,6,7,0,1,2].

# Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.

# You must write an algorithm with O(log n) runtime complexity.
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
        # find index k of rotation: binary search to find nums[i] > nums[i+1] -> k = i+1 
        n = len(nums)
        left, right = 0, n - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid
        k = left

        # find target: binary search on indices [k, k+1, .., n-1, 0, .., k-1]; indices modulu k?
        i, j = 0, n - 1

        while i+1 < j:
            l = (i + j) // 2
            lt = (l + k) % n

            # print(f'i={i}, j={j}, l={l}, lt={lt}')
            
            if nums[lt] < target:
                i = l
            elif nums[lt] > target:
                j = l
            else:
                return lt

        li = (i + k) % n
        lj = (j + k) % n

        if nums[li] == target:
            return li
        if nums[lj] == target:
            return lj
        return -1
        


sol = Solution()
print(sol.search([4,5,1,2,3], 5))