class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        
        strs.sort()
        first = strs[0]
        
        for i in range(len(first)):
            if first[i] != strs[-1][i]:
                return first[:i]
        return first
        