class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        left, right, maxLen = 0, 0, 0
        
        for i in range(len(s)):
            oddLen = self.expand(s, i, i)
            evenLen = self.expand(s, i, i+1)
            
            currLen = max(oddLen, evenLen)
            if currLen > maxLen:
                left = i - (currLen - 1) //2
                right = i + currLen //2
                maxLen = currLen
        return s[left: right + 1]
    
    def expand(self, s, left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right +=1
        return right - left - 1