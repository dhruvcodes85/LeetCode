import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        string = ''.join(char for char in s if char.isalnum()).lower()
        rev_str = string[::-1]
        return string == rev_str

sol = Solution()
print(sol.isPalindrome("A man, a plan, a canal: Panama"))