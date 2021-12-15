class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        
        res = []
        
        def dfs(nums, path):
            res.append(path)
            for i in range(len(nums)):
                dfs(nums[i+1:], path + [nums[i]])
        dfs(nums, [])
        return res
        