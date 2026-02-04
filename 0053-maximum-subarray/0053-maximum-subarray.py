class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # kadane's algorithm
        maxSum = float('-inf')
        sum = 0
        for i in range(len(nums)):
            sum += nums[i]
            if sum > maxSum:
                maxSum = sum
            if sum < 0:
                sum = 0

        return maxSum  