class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        cnt = 0
        for num in nums:
            if cnt == 0:
                cnt = 1
                ele = num
            elif ele == num: 
                cnt += 1
            else:
                cnt -= 1
            
        return ele
        