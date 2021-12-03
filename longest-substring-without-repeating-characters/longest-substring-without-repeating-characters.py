class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        substring, longest, start = set(), - math.inf, 0
        if len(s) == 0:
            return 0
        
        for end, char in enumerate(s):
            while char in substring:
                substring.remove(s[start])
                start +=1
            substring.add(char)
            longest = max(longest, end - start + 1)
        return longest
        