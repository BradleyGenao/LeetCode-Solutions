class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        
        left, right = 0, len(nums) - 1
        
        while left < right:
            mid = left + (right - left) // 2
            
            if (nums[0] <= target) ^ (nums[0] <= nums[mid]) ^ (target <= nums[mid]):
                right = mid
            else:
                left = mid + 1
        return left if target in nums[left:left+1] else -1