
# Given a string s, find the length of the longest substring 
# without duplicate characters.
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
      
      # idea: a single pass over s, maintain start-end indices
      # maintain dict with observerd characters: store index
      # new char: if in dict: update index, and start, end
      # if not in dict: add index, start fixed, end update

      start, end, maxs = 0, 0, 0

      # O(n) mem (worst case) => could reduce O(1) is only English letters
      app = {} 

      # O(n) time
      for i, c in enumerate(s):
        
        if c not in app:
            app[c] = i
        else:
            start = max(start, app[c] + 1)
            app[c] = i

        end += 1
        if maxs < end - start:
            maxs = end - start

      return maxs