class Solution:
    def maxPower(self, s: str) -> int:
        l, maxPow = 0, 0
        r = 1
        n = len(s)

        while(r < n):
            if s[l] == s[r]:
                r += 1
            else:
                l = r
                r += 1
            maxPow = max(maxPow, r - l)

        return maxPow

        return maxPow
