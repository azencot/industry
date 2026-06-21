# Given an integer array nums and an integer k, return true if nums 
# has a good subarray or false otherwise.

# A good subarray is a subarray where:

# its length is at least two, and
# the sum of the elements of the subarray is a multiple of k.
# Note that:

# A subarray is a contiguous part of the array.
# An integer x is a multiple of k if there exists an integer n such 
# that x = n * k. 0 is always a multiple of k.
class Solution(object):
    def checkSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        
        # O(n^2) time solution
        # if len(nums) < 2:
        #     return False

        # # prefixes = [nums[0]]
        # for num in nums[1:]:
        #     prefixes.append(prefixes[-1] + num)
        
        # for i, pref in enumerate(prefixes):
        #     if pref % k == 0 and i>0:
        #         return True

        #     for j in range(i-1):
        #         if (pref - prefixes[j]) % k == 0:
        #             return True

        # return False

        if len(nums) < 2:
            return False

        seen_remainders = {nums[0] % k: 0}
        curr_sum = nums[0]

        for i, num in enumerate(nums[1:], start=1):
            curr_sum += num
            curr_remainder = curr_sum % k

            if curr_remainder == 0:
                return True
            
            if curr_remainder in seen_remainders:
                if i - seen_remainders[curr_remainder] > 1:
                    return True
            else:
                seen_remainders[curr_remainder] = i

        return False




