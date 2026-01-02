class Solution:
    def reverse(self, x: int) -> int:
        is_negative = False

        if x < 0:
            x *= -1
            is_negative = True

        rev = 0
        while x > 0:
            rev = (rev * 10) + (x % 10)
            x = x // 10

        if rev > (2**31 - 1) or rev < -2**31:
            return 0

        return rev * -1 if is_negative else rev
        