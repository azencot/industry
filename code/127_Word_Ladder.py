# A transformation sequence from word beginWord to word endWord using a dictionary wordList is a sequence of words beginWord -> s1 -> s2 -> ... -> sk 
# such that:

# Every adjacent pair of words differs by a single letter.
# Every si for 1 <= i <= k is in wordList. Note that beginWord does not need to be in wordList.
# sk == endWord
# Given two words, beginWord and endWord, and a dictionary wordList, return the number of words in the shortest transformation sequence from beginWord 
# to endWord, or 0 if no such sequence exists.

class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """

        words_set = set()
        for i, word in enumerate(wordList):
            words_set.add(word)

        if endWord not in words_set:
            return 0

        length = 0
        curr_word = beginWord
        while curr_word != endWord:
            neighbors = []
            for i, curr_char in enumerate(curr_word):       # 10 iterations at most, O(1)
                for j in range(26):                         # 25 iterations, O(1)
                    tmp_char = chr(j + ord('a'))
                    if curr_char == tmp_char:
                        continue
                    tmp_word = list(curr_word)
                    tmp_word[i] = tmp_char
                    tmp_word = "".join(curr_word)
                    
                    if tmp_word in words_set:
                        neighbors.append(tmp_word)

            if len(neighbors) == 0:
                return 0

            length += 1
            for neighbor in neighbors:
                words_set.remove(neighbor)
                curr_word = neighbor            # recursive call


                
