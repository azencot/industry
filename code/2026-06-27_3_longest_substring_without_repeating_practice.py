# 3. Longest Substring Without Repeating Characters
#
# Given a string s, find the length of the longest substring without
# repeating characters.
#
# Example 1:
# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.
#
# Example 2:
# Input: s = "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.
#
# Example 3:
# Input: s = "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
#
# Constraints:
# - 0 <= s.length <= 5 * 10^4
# - s consists of English letters, digits, symbols and spaces.
#
# Link: https://leetcode.com/problems/longest-substring-without-repeating-characters/

# approach: scan s, maintain a dict of last occurance per seen char; maintain start of substr
# example: {'a': 0, 'b': 1, 'c': 2}
# max can be deduced by end of substr - start of substr (this is reset with every repeat)

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        si, max_len = 0, 0

        last_index = {}
        for i, c in enumerate(s):
            if c in last_index and last_index[c] >= si:
                si = last_index[c] + 1
            last_index[c] = i
            max_len = max(max_len, i - si + 1)

        return max_len


if __name__ == "__main__":
    tests = [
        ("abcabcbb", 3),
        ("bbbbb", 1),
        ("pwwkew", 3),
        ("", 0),
        (" ", 1),
        ("dvdf", 3),
        ("abba", 2),
    ]

    sol = Solution()
    for s, expected in tests:
        result = sol.lengthOfLongestSubstring(s)
        print(repr(s), result, "PASS" if result == expected else "FAIL")
