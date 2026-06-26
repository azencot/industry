# 153. Find Minimum in Rotated Sorted Array
# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/
#
# Suppose an array of length n sorted in ascending order is rotated between 1
# and n times. For example, the array nums = [0,1,2,4,5,6,7] might become:
#   [4,5,6,7,0,1,2] if it was rotated 4 times.
#   [0,1,2,4,5,6,7] if it was rotated 7 times.
#
# Given the sorted rotated array nums of UNIQUE elements, return the minimum
# element of this array.
#
# You must write an algorithm that runs in O(log n) time.
#
# Example 1:
#   Input:  nums = [3,4,5,1,2]
#   Output: 1   (original was [1,2,3,4,5], rotated 3 times)
#
# Example 2:
#   Input:  nums = [4,5,6,7,0,1,2]
#   Output: 0   (original was [0,1,2,4,5,6,7], rotated 4 times)
#
# Example 3:
#   Input:  nums = [11,13,15,17]
#   Output: 11  (original was [11,13,15,17], rotated 4 times)
#
# Constraints:
#   n == nums.length
#   1 <= n <= 5000
#   -5000 <= nums[i] <= 5000
#   All integers of nums are unique.
#   nums is sorted and rotated between 1 and n times.
#
# ---- Live-interview checklist ----
# restate -> clarify edge cases -> approach + complexity -> example -> code -> test
# Narrate invariants aloud (e.g. "if nums[mid] > nums[right], the min must be
# strictly to the right of mid").


# approach: this is binary search O(log n) time with O(1) mem with the change that we need to find the location of nums[i] > nums[i+1], and ret nums[i+1]

class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        if len(nums) == 1:
            return nums[0]
            
        si, ei, mi = 0, len(nums)-1, len(nums) // 2     # init start, end, middle indices

        while si + 1 < ei:
            # min in left half (don't need to handle == since numbers are unique)
            if nums[si] > nums[mi]:
                ei = mi
            # min in right half
            else:
                si = mi
            mi = (si + ei) // 2

        if nums[ei] < nums[ei-1]:
            return nums[ei]
        else:
            return nums[0]


if __name__ == "__main__":
    s = Solution()

    print(s.findMin([3, 4, 5, 1, 2]))         # expect 1
    print(s.findMin([4, 5, 6, 7, 0, 1, 2]))   # expect 0
    print(s.findMin([11, 13, 15, 17]))        # expect 11 (not rotated / full rotation)
    print(s.findMin([2, 1]))                  # expect 1
    print(s.findMin([1]))                     # expect 1 (single element)
