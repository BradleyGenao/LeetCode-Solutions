class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        pos = 0
        for i, num in enumerate(nums):
            if num != 0:
                if i != pos:
                    nums[i], nums[pos] = nums[pos], nums[i]
                pos +=1
        return nums