from collections import Counter
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p) > len(s):
            return []
        
        p_count = Counter(p)
        s_count = Counter(s[:len(p) - 1])
        indices =  []
        for i in range(len(p) - 1, len(s)):
            s_count[s[i]] += 1 #s[i] is the right most character

            if p_count == s_count:
                indices.append(i - len(p) + 1)
            
            left_char = s[i - len(p) + 1] # i - len(p) + 1 tracks the starting index of window
            s_count[left_char] -= 1
            if s_count[left_char] == 0:
                del s_count[left_char]

        return indices