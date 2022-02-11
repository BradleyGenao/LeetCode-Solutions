class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        held, sold, reset = -math.inf, -math.inf, 0
        
        for price in prices:
            
            pre_sold = sold
            sold = held + price
            held = max(held, reset- price)
            reset = max(reset, pre_sold)
        
        return max(sold, reset)
        