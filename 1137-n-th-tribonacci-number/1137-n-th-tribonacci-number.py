class Solution:
    def tribonacci(self, n: int) -> int:
        
        if n <3:
            return 1 if n else 0
        
        
        memo = {}
        def helper(n):
            if n in memo:
                return memo[n]
            
            if n <3:
                return 1 if n else 0
            
            memo[n] = helper(n-1) + helper(n-2) + helper(n-3)
            return memo[n]
        return helper(n)
        