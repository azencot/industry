#  Given an integer array nums, return true if any value appears at 
# least twice in the array, and return false if every element is distinct.
class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        
        # one option would be to sort, but we pay O(n logn)

        # another option is to use a hash with amortized O(n)
        # very similar to 2sum, we can insert new keys/access prev keys in AO(1)
        s = set()

        for val in nums:
            if val in s:
                return True
            
            s.add(val)
        return False