import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        str = re.sub(r'[^a-zA-Z0-9]', '', s)
        rev_str = str[::-1]
        if str.lower() == rev_str.lower():
            return True
        else:
            return False
sol = Solution()
print(sol.isPalindrome("A man, a plan, a canal: Panama"))