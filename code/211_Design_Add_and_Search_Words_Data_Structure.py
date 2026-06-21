# Design a data structure that supports adding new words and finding if a string matches any previously added string.

# Implement the WordDictionary class:

# WordDictionary() Initializes the object.
# void addWord(word) Adds word to the data structure, it can be matched later.
# bool search(word) Returns true if there is any string in the data structure that matches word or false otherwise. word may contain dots '.' where dots can
#  be matched with any letter.

class TrieNode(object):
    def __init__(self):
        self.endOfWord = False
        self.children = {}

class WordDictionary(object):

    def __init__(self):
        self.root = {}

    def addWord(self, word):
        """
        :type word: str
        :rtype: None
        """

        curr_dict = self.root

        for i, c in enumerate(word):
            if c in curr_dict:
                curr_dict = curr_dict[c].children
                if i == len(word) - 1:
                    curr_dict[c].endOfWord = True
            else:
                node = TrieNode()
                if i == len(word) - 1:
                    node.endOfWord = True
                curr_dict[c] = node
                curr_dict = node.children

    def search(self, word):
        """
        :type word: str
        :rtype: bool
        """

        def scan_suffix(curr_word, curr_dict):

            if len(curr_word) == 1:
                if curr_word in curr_dict:
                    return curr_dict[curr_word].endOfWord
                else:
                    return False

            for i, c in enumerate(curr_word):
                if c == '.':
                    for tmp_c in curr_dict:
                        ret = scan_suffix(curr_word[i:], curr_dict[tmp_c])
                        if ret == True:
                            return True

                if c not in curr_dict:
                    return False
                else:
                    curr_dict = curr_dict[c].children

        # need DFS for every .
        return scan_suffix(word, self.root)