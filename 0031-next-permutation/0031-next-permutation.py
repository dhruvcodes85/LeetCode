class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        
        idx = -1
        for i in range(len(nums) - 2, -1, -1): ## -2 because, we will check last 2 numbers, hence not running through an index out of bound error
            if nums[i] < nums[i + 1]:
                idx = i
                break
        # print(idx)
        
        if idx == -1:
            nums.reverse()
            return

        for i in range(len(nums) - 1, idx, -1):
            if nums[i] > nums[idx]:
                print(nums[idx])
                nums[i], nums[idx] = nums[idx], nums[i]
                break
            
        nums[idx+1:] = reversed(nums[idx+1:])


        