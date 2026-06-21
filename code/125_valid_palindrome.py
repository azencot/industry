# A phrase is a palindrome if, after converting all uppercase letters into 
# lowercase letters and removing all non-alphanumeric characters, it reads 
# the same forward and backward. Alphanumeric characters include letters 
# and numbers.

# Given a string s, return true if it is a palindrome, or false otherwise.
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """

        s = ''.join(c.lower() for c in s if c.isalnum()) # O(n) mem
        
        # solution should be based on two pointers (from start & end)
        for i in range(len(s)):
            j = len(s) - i - 1

            # stop
            if i >= j:
                return True

            # not palindrome: lc(s[i]) != lc(s[j])
            if s[i] != s[j]:
                return False

        # edge case if s is empty
        return True

# sol = Solution()
# print(sol.isPalindrome("race a car"))