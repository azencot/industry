# 567. Permutation in String
# https://leetcode.com/problems/permutation-in-string/
#
# Difficulty: Medium
# Tags: Hash Table, Two Pointers, String, Sliding Window
#
# Given two strings s1 and s2, return true if s2 contains a permutation of s1,
# or false otherwise.
#
# In other words, return true if one of s1's permutations is the substring of s2.
#
# Example 1:
#   Input: s1 = "ab", s2 = "eidbaooo"
#   Output: true
#   Explanation: s2 contains one permutation of s1 ("ba").
#
# Example 2:
#   Input: s1 = "ab", s2 = "eidboaoo"
#   Output: false
#
# Constraints:
#   - 1 <= s1.length, s2.length <= 10^4
#   - s1 and s2 consist of lowercase English letters.
#
# --- Timed drill: 2026-06-24 (25 min) ---


# a potential solution:
# 1) create a hash table (dict) of all chars in s1 and #appearances (counter)
# 2) iterate over s2: there are two modes: in permutation or not; if not, dict should be orig (after init); if in, then, per char, check if in hash; if yes, decrease counter, if not init dict

# problem: after modifying dict, how to revert decreases? I can dict.copy(), not sure if this optimal

class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        
        # create hash table for s1
        freq = {}
        for c in s1:
            freq[c] = freq.get(c, 0) + 1

        # iterate over s2
        i, le = 0, 0
        substr, freq2, count = False, freq.copy(), 0
        while i < len(s2):
            c = s2[i]

            if substr and (c not in freq2 or freq2[c] <= 0):
                i = le + 1
                substr, freq2, count = False, freq.copy(), 0
                continue

            if c in freq2 and not substr:
                substr, le = True, i
            
            if c in freq2:
                freq2[c] -= 1
                count += 1

            if count == len(s1):
                return True

            i += 1         

        return False


if __name__ == "__main__":
    sol = Solution()
    assert sol.checkInclusion("ab", "eidbaooo") is True
    assert sol.checkInclusion("ab", "eidboaoo") is False
    assert sol.checkInclusion("a", "a") is True
    assert sol.checkInclusion("adc", "dcda") is True
    assert sol.checkInclusion("ab", "aab") is True
    print("ok")
