class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        n = len(boxes)
        answer = [0] * n
        left, right, steps = 0, 0 ,0 
        
        for i, box in enumerate(boxes):
            if box == '1':
                steps +=i
                right+=1
        
        for j, box in enumerate(boxes):
            answer[j] = steps
            
            
            if box == '1':
                right -=1
                left +=1
            
            steps +=left
            steps -=right
        
        
        return answer