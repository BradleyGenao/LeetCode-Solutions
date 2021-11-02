class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        self.rec(nums, [], 0, ans)
        return ans
    
    def rec(self, nums, curr, index, ans):
        
        if len(nums) ==index:
            ans.append(curr)
        else:
            for i in range(len(curr) + 1):
                new_perm = list(curr)
                new_perm.insert(i, nums[index])
                self.rec(nums, new_perm, index+1, ans)
        