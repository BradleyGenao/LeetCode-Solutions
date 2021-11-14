class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        
        
        """
        Need to use unique paris - *use pointers stating from left and right
        
        have to take min sums - *sort list to get the min pairs
        
        [3, 5, 2, 3] = [2,3,3,5] = minpairs(2, 5) ,(3, 3)
        
        Space and Time: O(NlogN) due to the sorting fo nums
        """
        # O(nlogn)
        nums = sorted(nums)
        left, right = 0, len(nums) - 1
        max_sum = - math.inf
        # O(n)
        while left < right:
            max_sum = max(max_sum, nums[left] + nums[right])
            left +=1
            right-=1
        return max_sum
            