class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        
        unique = set()
        start = 0
        longest = 0
        for end, char in enumerate(s):
            while char in unique:
                unique.remove(s[start])
                start += 1
            unique.add(char)
            longest = max(longest, end - start + 1)
        return longest