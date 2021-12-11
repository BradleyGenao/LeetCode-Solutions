class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
        
        
        
        
        
        if len(nums) == 1:
            return nums[0]
        
        half = len(nums) //2 
        left = nums[:half]
        right = nums[half:]
        
        for num in left:
            if nums.count(num) == 1:
                return num
        
        for num in right:
            if nums.count(num) == 1:
                return num