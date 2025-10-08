class Solution(object):
    def reverse(self, x):
        rev = 0
        if x < 0:
            rev = int(str(x)[1:][::-1]) * -1
        else:
            rev = int(str(x)[::-1])
        
        if rev > 2 ** 31 - 1 or rev < -2 ** 31:
            return 0
        
        return rev
        
rev = Solution()
rev.reverse(123)