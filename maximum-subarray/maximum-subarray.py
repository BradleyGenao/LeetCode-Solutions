class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        curr_sum, max_sub = 0, -math.inf
        
        for num in nums:
            curr_sum += num
            
            max_sub = max(max_sub, curr_sum)
            
            if curr_sum < 0:
                curr_sum = 0
        return max_sub
        
        