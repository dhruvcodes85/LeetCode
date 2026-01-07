class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        n = len(nums)
        sum = 0
        for i in range(k):
            sum += nums[i]

        maxSum = sum
        for i in range(k, n):
            sum -= nums[i - k]
            sum += nums[i]
            maxSum = max(maxSum, sum)

        return maxSum / k