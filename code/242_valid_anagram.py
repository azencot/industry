# Given two strings s and t, return true if t is an anagram of s, and 
# false otherwise.
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # similar to 2sum, main difference is we count how many chars we see
        # and we remove from hash as we traverse t

        if len(s) != len(t):
            return False

        hash = {}

        # store s, AO(n)
        for c in s:
            hash[c] = hash.get(c, 0) + 1

        # traverse t, AO(m)
        for c in t:
            if c not in hash:
                return False
            hash[c] -= 1
            if hash[c] < 0:
                return False

        return True