class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        preSum = 0
        cnt = 0
        mpp = {}
        mpp[0] = 1

        for i in range(len(nums)):
            preSum += nums[i]
            remove = preSum - k
            if remove in mpp:
                cnt += mpp[remove]
            mpp[preSum] = mpp.get(preSum, 0) + 1

        return cnt