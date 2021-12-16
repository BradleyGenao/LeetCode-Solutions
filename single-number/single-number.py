class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
        xor_check = 0
        
        for num in nums:
            xor_check ^= num
        return xor_check
        