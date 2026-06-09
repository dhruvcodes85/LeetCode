class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        s = set()
        longest = 1
        for num in nums:
            s.add(num)

        for num in s:
            if (num-1) not in s:
                cnt = 0
                x = num
                while x in s:
                    x += 1
                    cnt += 1
                longest = max(longest, cnt)

        return longest