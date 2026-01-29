### Using the dutch national flag algorithm
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        n = len(nums)
        low = 0
        mid = 0
        high = n - 1

        while mid <= high:   
                #their is no unsorted portion remaining when mid equals high
            if nums[mid] == 0:
                nums[low], nums[mid] = nums[mid], nums[low]
                low += 1
                mid += 1
            elif nums[mid] == 1:  # 1 is already present at the position which contains all 1 just move mid to the right
                mid += 1 
            else:
                nums[mid], nums[high] = nums[high], nums[mid]
                high -= 1
                # why mid was not incremented 
                ## as mid to high contains unsorted numbers 
                ## hence if we place 2 at its correct position mid index will now have a number which is already at the unsorted portion

