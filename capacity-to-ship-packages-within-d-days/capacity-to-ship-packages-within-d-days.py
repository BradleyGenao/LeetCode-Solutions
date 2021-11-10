class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        
        """
        
        Using Binary Search
        
        left, right = min to be the max(weights) at least it holds the biggest and max to be the sum(weights) it can take all weights combined
        
        mid = left + (right - left) // 2
        
        send mid to feasble function(capacity) if true set right to mid
        
        with the capcity need a total and day variable 
        iterate for weight in weights adding to total 
        check total is less than capacity
        if not set total to weight 
        add 1 to day
        if day is greate than days return false
        return true
        
        else left = mid + 1
        
        
        
        """
        
        
        
        def check_cap(capacity):
            total, day = 0, 1
            for weight in weights:
                total += weight
                if total > capacity:
                    total = weight
                    day +=1
                    if day >days:
                        return False
            return True
        
        
        left, right = max(weights), sum(weights)
        
        while left < right:
            mid = left + (right - left) //2
            if check_cap(mid):
                right = mid
            else:
                left = mid + 1
        return left