"""
15. 3Sum
https://leetcode.com/problems/3sum/

Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]]
such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

Example 1:
    Input: nums = [-1,0,1,2,-1,-4]
    Output: [[-1,-1,2],[-1,0,1]]

Example 2:
    Input: nums = [0,1,1]
    Output: []

Example 3:
    Input: nums = [0,0,0]
    Output: [[0,0,0]]

Constraints:
    3 <= len(nums) <= 3000
    -10**5 <= nums[i] <= 10**5
"""

# approach: scan nums, for num, solve 2sum for -num; need to split nums at pivot; Complexity is O(n^2) time and O(n) mem
# can we do better that O(n^2) time? 

class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        nums.sort()
        n = len(nums)

        ret = []

        for i in range(n-2):
            # skip duplicates
            if i>0 and nums[i] == nums[i-1]:
                continue
            if nums[i] > 0:
                break
            
            lo, hi = i+1, n-1
            while lo < hi:
                s = nums[i] + nums[lo] + nums[hi]
                if s == 0:
                    ret.append([nums[i], nums[lo], nums[hi]])

                    lo, hi = lo + 1, hi - 1
                    while lo < hi and nums[lo] == nums[lo-1]:
                        lo += 1 

                    while lo < hi and nums[hi] == nums[hi+1]:
                        hi -= 1 
                elif s < 0:
                    lo += 1
                else:
                    hi -= 1



        return ret


if __name__ == "__main__":
    sol = Solution()

    assert sorted(map(sorted, sol.threeSum([-1, 0, 1, 2, -1, -4]))) == sorted(
        map(sorted, [[-1, -1, 2], [-1, 0, 1]])
    )
    assert sol.threeSum([0, 1, 1]) == []
    assert sol.threeSum([0, 0, 0]) == [[0, 0, 0]]

    print("all tests passed")
