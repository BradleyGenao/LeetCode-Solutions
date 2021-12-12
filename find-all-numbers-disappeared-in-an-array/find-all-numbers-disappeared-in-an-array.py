class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        
        hashset = set(nums)
        ans = []
        for num in range(1, len(nums) + 1):
            if num not in hashset:
                ans.append(num)
        return ans
        