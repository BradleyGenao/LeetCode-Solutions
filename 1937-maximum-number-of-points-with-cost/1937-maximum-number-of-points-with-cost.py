class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        
        dp = [0] * (len(points[0]))
        
        for line in points:
            for i in range(1, len(line)):
                dp[i] = max(dp[i], dp[i-1] - 1)
                dp[-i-1] = max(dp[-i-1], dp[-i] -1 )
            for i in range(len(line)):
                dp[i] += line[i]
        return max(dp)