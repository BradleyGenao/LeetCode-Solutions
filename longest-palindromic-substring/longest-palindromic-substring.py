class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        
        left, right, max_len = 0, 0, 0
        
        for i in range(len(s)):
            odd_len = self.expand(s, i, i)
            even_len = self.expand(s, i, i+1)
            
            curr_len = max(odd_len, even_len)
            
            if curr_len > max_len:
                left = i - (curr_len - 1) // 2
                right = i + curr_len //2
                max_len = curr_len
            
        return s[left: right + 1]
    
    def expand(self, s, left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -=1
            right +=1
        return right - left - 1
        