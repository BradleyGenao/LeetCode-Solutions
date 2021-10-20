class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        
        answer = []
        self.permute_rec(nums, 0, [], answer)
        return answer
    
    def permute_rec(self, nums, index, curr_perm, answer):
        if len(nums) == index:
            answer.append(curr_perm)
        else:
            for i in range(len(curr_perm) + 1):
                new_perm = list(curr_perm)
                new_perm.insert(i, nums[index])
                self.permute_rec(nums, index+1, new_perm, answer)
        
        
        