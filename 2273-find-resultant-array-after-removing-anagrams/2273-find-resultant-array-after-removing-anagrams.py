from collections import Counter

class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        write = 0 #the first letter is always a non anagram

        for i in range(1, len(words)):
            if Counter(words[i]) != Counter(words[write]): #finding non-anagrams to overwrite over anagrams
                words[write + 1] = words[i]
                write += 1

        return words[:write + 1]
