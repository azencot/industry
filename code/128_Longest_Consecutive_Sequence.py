# Given an unsorted array of integers nums, return the length of the longest 
# consecutive elements sequence.

# You must write an algorithm that runs in O(n) time.
class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        # idea: main a dict of nums and count consecutive seq
        # for num in nums: check if its cons. numbers in dict: if yes, update seq start
        # store max seen len

        # dict saves seq start; another dict saves length (keys are seq start)

        # maintain a set of possible starts
        # maintain a dict for seen numbers 

        s = set(nums)

        max_len = 0
        for num in s:
            # grow forward
            if num - 1 not in s:
                curr_len, curr_num = 0, num
                while curr_num in s:
                    curr_len += 1
                    curr_num += 1

                if max_len < curr_len:
                    max_len = curr_len

        return max_len

sol = Solution()
sol.longestConsecutive([1,0,1,2])