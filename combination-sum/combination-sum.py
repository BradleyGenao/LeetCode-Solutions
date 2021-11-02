class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        self.dfs(candidates, target, [], ans)
        return ans
    
    def dfs(self, nums, target, path, ans):
        if target < 0:
            return 
        if target == 0:
            ans.append(path)
            return
        for i in range(len(nums)):
            self.dfs(nums[i:], target-nums[i], path +[nums[i]], ans)