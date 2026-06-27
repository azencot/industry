# 211. Design Add and Search Words Data Structure
# https://leetcode.com/problems/design-add-and-search-words-data-structure/
#
# Design a data structure that supports adding new words and finding if a
# string matches any previously added string.
#
# Implement the WordDictionary class:
#   WordDictionary() initializes the object.
#   void addWord(word) adds word to the data structure.
#   bool search(word) returns true if there is any string in the data structure
#   that matches word. The word may contain dots '.', where dots can be matched
#   with any letter.
#
# Example:
#   Input:
#     ["WordDictionary", "addWord", "addWord", "addWord", "search", "search", "search", "search"]
#     [[], ["bad"], ["dad"], ["mad"], ["pad"], ["bad"], [".ad"], ["b.."]]
#   Output:
#     [null, null, null, null, false, true, true, true]
#
# Constraints:
#   1 <= word.length <= 25
#   word in addWord consists of lowercase English letters.
#   word in search consists of '.' or lowercase English letters.
#   There will be at most 2 dots in word for search queries.
#   At most 10^4 calls will be made to addWord and search.
#
# ---- Live-interview checklist ----
# restate -> clarify edge cases -> approach + complexity -> example -> code -> test
# Narrate invariants aloud (e.g. "each trie node represents a prefix; wildcard
# search branches only when the current character is '.''").


# approach: construct a Trie data structure: root points to char, child points to next char, etc; adding word is traversal over the Trie (adding chars only if needed)
# search is plain traversal (while taking care of . case)
# Complexity: c'tor: probably O(1) mem + time; addWord: probably O(k) mem + time, where k is word length; search: probably O(k) time, O(1) mem

class trieNode(object):
    def __init__(self, val):
        self.val = val
        self.childNodes = {}        # child nodes are stored by {char: trieNode}


class WordDictionary(object):

    def __init__(self):
        self.root = trieNode('')

    def addWord(self, word):
        """
        :type word: str
        :rtype: None
        """
        currNode = self.root
        for c in word:
            if c not in currNode.childNodes:
                currNode.childNodes[c] = trieNode(c)
            currNode = currNode.childNodes[c]

    
    def search_subword(self, word, nodes):
        if word == '':
            return True

        for node in nodes:

            currNode = node
            for i, c in enumerate(word):
                if c == '.':
                    return self.search_subword(word[i+1:], currNode.childNodes)
                
                if c in currNode.childNodes:
                    currNode = currNode.childNodes[c]
                else:
                    return False
            return True
        return False


    def search(self, word):
        """
        :type word: str
        :rtype: bool
        """
        return self.search_subword(word, [self.root])

            
if __name__ == "__main__":
    wd = WordDictionary()
    wd.addWord("bad")
    wd.addWord("dad")
    wd.addWord("mad")

    print(wd.search("pad"))  # expect False
    print(wd.search("bad"))  # expect True
    print(wd.search(".ad"))  # expect True
    print(wd.search("b.."))  # expect True
    print(wd.search("b.d"))  # expect True
    print(wd.search("..d"))  # expect True
    print(wd.search("..."))  # expect True
    print(wd.search("....")) # expect False
