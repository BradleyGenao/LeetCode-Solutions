class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        
        
        def dfs(nums, path):
            res.append(path)
            for i in range(len(nums)):
                dfs(nums[i+ 1:], path + [nums[i]])
        
        
        
        
        
        res = []
        dfs(nums, [])
        return res
        