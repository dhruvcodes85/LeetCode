class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        n = len(intervals)
        ans = []
        for i in range(n):
            if not ans or intervals[i][0] > ans[-1][1]:
                ## start fresh
                ans.append(intervals[i])
            else:
                ans[-1][1] = max(intervals[i][1], ans[-1][1])

        return ans

        