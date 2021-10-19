class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        
        result = []
        self.find_perms(nums, 0, [], result)
        return result
    
    def find_perms(self,nums, index, curr_perm, result ):
        if len(nums) == index:
            result.append(curr_perm)
        else:
            for i in range(len(curr_perm) + 1):
                new_perm = list(curr_perm)
                new_perm.insert(i, nums[index])
                self.find_perms(nums, index+1, new_perm, result)
        
                
        