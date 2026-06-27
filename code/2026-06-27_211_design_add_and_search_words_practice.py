# 211. Design Add and Search Words Data Structure
#
# Design a data structure that supports adding new words and finding if a string
# matches any previously added string.
#
# Implement the WordDictionary class:
# - WordDictionary() Initializes the object.
# - void addWord(word) Adds word to the data structure.
# - bool search(word) Returns True if there is any string in the data structure
#   that matches word, or False otherwise. word may contain dots "." where
#   dots can be matched with any letter.
#
# Example:
# Input:
# ["WordDictionary","addWord","addWord","addWord","search","search","search","search"]
# [[],["bad"],["dad"],["mad"],["pad"],["bad"],[".ad"],["b.."]]
# Output:
# [null,null,null,null,false,true,true,true]
#
# Constraints:
# - 1 <= word.length <= 25
# - word in addWord consists of lowercase English letters.
# - word in search consist of "." or lowercase English letters.
# - There will be at most 2 dots in search.
# - At most 10^4 calls in total will be made to addWord and search.
#
# Link: https://leetcode.com/problems/design-add-and-search-words-data-structure/


class CharsNode(object):
    def __init__(self):
        self.chars = {}
        self.isEnd = False

class WordDictionary(object):
    def __init__(self):
        self.words = CharsNode()

    def addWord(self, word):
        """
        :type word: str
        :rtype: None
        """
        currNode = self.words
        for c in word:
            if c not in currNode.chars:
                currNode.chars[c] = CharsNode()
            currNode = currNode.chars[c]
        currNode.isEnd = True

    def search(self, word):
        """
        :type word: str
        :rtype: bool
        """

        def do_dfs(word, node):
            if len(word) == 0:
                return node.isEnd

            currNode = node
            for i, c in enumerate(word):
                if c == '.':
                    for char in currNode.chars:
                        if do_dfs(word[i+1:], currNode.chars[char]):
                            return True
                    return False
                if c not in currNode.chars:
                    return False
                currNode = currNode.chars[c]

            return currNode.isEnd

        
        return do_dfs(word, self.words)


if __name__ == "__main__":
    wd = WordDictionary()
    wd.addWord("bad")
    wd.addWord("dad")
    wd.addWord("mad")

    tests = [
        ("pad", False),
        ("bad", True),
        (".ad", True),
        ("b..", True),
        ("...", False),
        ("ba.", True),
        ("m.d", True),
    ]

    for word, expected in tests:
        result = wd.search(word)
        print(word, result, "PASS" if result == expected else "FAIL")
