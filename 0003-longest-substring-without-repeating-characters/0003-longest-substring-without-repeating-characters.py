class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        mpp = {chr(i): -1 for i in range(256)}
        l, r, maxLen = 0, 0, 0
        n = len(s)
        while(r < n):
            if mpp[s[r]] != -1:    #char present in the map
                if mpp[s[r]] >= l: #move the window one step ahead then the repeating char
                    l = mpp[s[r]] + 1
            leng = r - l + 1
            maxLen = max(leng, maxLen)
            mpp[s[r]] = r
            r += 1

        return maxLen
