class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        
        left = 0
        right = len(height) -1
        max_area = -math.inf
        
        while left <= right:
            area = abs(right-left) * min(height[left], height[right])
            
            max_area = max(area, max_area)
            if height[left] > height[right]:
                right -=1
            else:
                left +=1
                
            
        return max_area        