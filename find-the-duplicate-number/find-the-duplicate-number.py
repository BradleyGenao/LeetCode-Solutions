import collections

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        
        count_dict = defaultdict(int)
        
        for num in nums:
            count_dict[num] += 1
            
            if count_dict[num] == 2:
                return num
        
            
        