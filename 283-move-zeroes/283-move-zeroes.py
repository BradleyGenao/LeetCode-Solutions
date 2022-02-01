class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        last_zero = 0
        
        for i, num in enumerate(nums):
            if num != 0:
                if i != last_zero:
                    nums[i], nums[last_zero] = nums[last_zero], nums[i]
                last_zero +=1
        return nums