class Solution:
    def isPalindrome(self, x: int) -> bool:
        original = x
        rev = 0
        if x < 0:
            return False
        else:
            while x > 0:
                rev = (rev * 10) + (x % 10)
                x = x // 10
            if rev == original:
                return True
            else:
                return False