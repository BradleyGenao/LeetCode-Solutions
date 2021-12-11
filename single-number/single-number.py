class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        counter = collections.Counter(nums)
        
        if len(nums) == 1:
            return nums[0]
        
        for num, count in counter.items():
            if count == 1:
                return num
        