class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        
        
        
        counter = collections.Counter(nums)
        
        for count in counter.values():
            if count > 1:
                return True
        return False
        
        
        
        