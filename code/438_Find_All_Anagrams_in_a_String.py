# Given two strings s and p, return an array of all the start 
# indices of p's anagrams in s. You may return the answer in any order.
class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        n, m = len(s), len(p)

        if m > n:
            return []

        # only lowercase English letters
        pl = [0] * 26
        
        for i in range(m):
            pl[ord(p[i]) - ord('a')] += 1

        sl = [0] * 26
        anagrams = []
        for i in range(n):
            sl[ord(s[i]) - ord('a')] += 1

            if i >= m:
                sl[ord(s[i - m]) - ord('a')] -= 1

            if pl == sl:
                anagrams.append(i - m + 1)

        return anagrams