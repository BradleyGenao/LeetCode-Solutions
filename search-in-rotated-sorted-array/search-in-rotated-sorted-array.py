class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        
        lo, hi = 0, len(nums) -1
        
        while lo < hi:
            mid = lo + (hi -lo) // 2
            
            if (nums[0] <= nums[mid]) ^ (nums[0] <= target) ^ (target <= nums[mid]):
                hi = mid
            else:
                lo = mid + 1
        return lo if target in nums[lo:lo+1] else -1
        