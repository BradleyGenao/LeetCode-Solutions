class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        O(nlogn + n^2)
        Time O(n^2) Space O(n)
        """
        
        triplets = []
        sorted_nums = sorted(nums)
        
        for i in range(len(nums) -2 ):
            left, right = i + 1, len(nums) - 1
            
            while left < right:
                triplet = [sorted_nums[i] , sorted_nums[left] , sorted_nums[right]]
                curr_sum = sum(triplet)
                if curr_sum == 0:
                    triplets.append(triplet)
                    left +=1
                    right -=1
                elif curr_sum < 0:
                    left +=1
                elif curr_sum > 0:
                    right -=1
        
        
        answer = []
        for triplet in triplets:
            if triplet not in answer:
                answer.append(triplet)
        return answer
        