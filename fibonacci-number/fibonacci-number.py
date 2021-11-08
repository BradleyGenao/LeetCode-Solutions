class Solution:
    def fib(self, n: int) -> int:
        
        memo = {}
        memo[0] = 0
        memo[1] = 1
        
        def fib(n):
            if n in memo:
                return memo[n]
            else:
                memo[n] = fib(n-1)+ fib(n-2)
                return memo[n]
        return fib(n)