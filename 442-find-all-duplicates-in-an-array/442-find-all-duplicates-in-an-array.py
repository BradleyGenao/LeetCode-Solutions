class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        
        
        for num in nums:
            num = abs(num)
            if nums[num-1] < 0:
                
                yield num
            
            nums[num-1] *= -1
        
        
        
        