class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        
        compare = {}
        
        for i in range(len(nums) + 1):
            compare[i] = 0
        
        for num in compare:
            if num not in nums:
                return num
        