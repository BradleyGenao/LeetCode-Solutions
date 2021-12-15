class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        
        uniques = set()
        start = 0
        max_len = 0
        
        for end in range(len(s)):
            while s[end] in uniques:
                uniques.remove(s[start])
                start +=1
            uniques.add(s[end])
            max_len = max(max_len, end - start + 1)
        return max_len
        