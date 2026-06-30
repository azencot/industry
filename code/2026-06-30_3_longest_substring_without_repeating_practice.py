# LeetCode 3. Longest Substring Without Repeating Characters
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
# 0 <= len(s) <= 5 * 10^4
# s consists of English letters, digits, symbols and spaces.
#
# LeetCode: https://leetcode.com/problems/longest-substring-without-repeating-characters/

# approach: store in hash last appearance of character; maintain substr start
# complexity: O(len(s)) time, O(len(s)) mem

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        last_seen = {}

        max_len, si = 0, 0
        for i, c in enumerate(s):
            if c in last_seen and last_seen[c] >= si:
                si = last_seen[c] + 1
            last_seen[c] = i

            max_len = max(max_len, i - si + 1)

        return max_len


if __name__ == "__main__":
    solution = Solution()
    print(solution.lengthOfLongestSubstring("abcabcbb"))  # 3
    print(solution.lengthOfLongestSubstring("bbbbb"))  # 1
    print(solution.lengthOfLongestSubstring("pwwkew"))  # 3
    print(solution.lengthOfLongestSubstring(""))  # 0
