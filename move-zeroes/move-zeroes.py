class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        anchor = 0
        
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[anchor], nums[i] = nums[i], nums[anchor]
                anchor +=1
        return nums