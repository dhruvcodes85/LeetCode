class Solution:
    def validPalindrome(self, s: str) -> bool:
        for remove_index in range(len(s)):
            new_str = s[:remove_index] + s[remove_index + 1:]
            rev_str = new_str[::-1]
            if new_str == rev_str:
                return True
        return False 