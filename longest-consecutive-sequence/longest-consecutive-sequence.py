class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seq_set, result = set(nums), 0
        
        for num in nums:
            if num - 1 in seq_set:
                continue
            count = 0
            while num + count in seq_set:
                count+=1
            result = max(count, result)
        return result
        