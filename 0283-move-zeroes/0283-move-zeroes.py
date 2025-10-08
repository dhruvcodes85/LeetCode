class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        
        all_zero_indices = [i for i, zero in enumerate(nums) if zero == 0]

        for i in all_zero_indices[::-1]:
            nums.append(0)
            nums.pop(i)
        