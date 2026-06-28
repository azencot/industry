"""
560. Subarray Sum Equals K
https://leetcode.com/problems/subarray-sum-equals-k/

Given an array of integers nums and an integer k, return the total number of
subarrays whose sum equals to k.

A subarray is a contiguous non-empty sequence of elements within an array.

Example 1:
    Input: nums = [1,1,1], k = 2
    Output: 2

Example 2:
    Input: nums = [1,2,3], k = 3
    Output: 2

Example 3:
    Input: nums = [1,-1,0], k = 0
    Output: 3

Constraints:
    1 <= len(nums) <= 2 * 10**4
    -1000 <= nums[i] <= 1000
    -10**7 <= k <= 10**7
"""


class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        prefix_count = {0: 1}
        curr_sum = 0
        count = 0

        for num in nums:
            curr_sum += num                                             # current prefix

            if curr_sum - k in prefix_count:
                count += prefix_count[curr_sum - k]

            prefix_count[curr_sum] = prefix_count.get(curr_sum, 0) + 1  # track current prefix count

        return count




if __name__ == "__main__":
    sol = Solution()

    assert sol.subarraySum([1, 1, 1], 2) == 2
    assert sol.subarraySum([1, 2, 3], 3) == 2
    assert sol.subarraySum([1, -1, 0], 0) == 3
    assert sol.subarraySum([0, 0, 0], 0) == 6
    assert sol.subarraySum([-1, -1, 1], 0) == 1

    print("all tests passed")
