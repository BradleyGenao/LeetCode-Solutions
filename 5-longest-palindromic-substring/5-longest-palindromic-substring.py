class Solution:
    def longestPalindrome(self, s: str) -> str:
        left, right = 0, 0
        max_len = 0
    
        def expand(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -=1
                right +=1
            return right - left - 1

   
        for i in range(len(s)):
            odd = expand(i, i)
            even = expand(i, i+1)
            curr_len = max(odd, even)
            if curr_len > max_len:
                left = i - (curr_len-1) // 2
                right = i + curr_len // 2
                max_len = curr_len
        return s[left:right+1]

        
        
        
        
        