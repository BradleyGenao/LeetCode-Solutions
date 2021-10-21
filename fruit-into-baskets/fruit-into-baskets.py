import collections

class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        
        basket = defaultdict(int)
        win_start = 0
        max_len = - math.inf
        
        for win_end in range(len(fruits)):
            right = fruits[win_end]
            basket[right] +=1
            
            while len(basket) > 2:
                left = fruits[win_start]
                basket[left] -= 1
                if basket[left] == 0:
                    del basket[left]
                win_start +=1
            max_len = max(max_len, win_end - win_start + 1)
        
        return max_len
            
        
        
        