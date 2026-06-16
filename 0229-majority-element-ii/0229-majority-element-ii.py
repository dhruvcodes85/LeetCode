class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        mpp = {}
        ans = []
        n = len(nums)
        for i in nums:
            mpp[i] = mpp.get(i, 0) + 1
        
        for ele, cnt in mpp.items():
            if cnt > n/3:
                ans.append(ele)

        return ans