# Given an array of strings strs, group the anagrams together. You can 
# return the answer in any order.
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        
        groups = {}

        # O(n) time, where n is #words
        for word in strs:
            # O(k log k) time, where k is the avg word length
            key = tuple(sorted(word))
            if key not in groups:
                groups[key] = []
            groups[key].append(word)

        return list(groups.values())
