import collections

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        return self.build_dict(s) == self.build_dict(t)
        
        
    
    
    def build_dict(self, string):
        ana_dict = defaultdict(int)
        
        
        for char in string:
            ana_dict[char] +=1
        return ana_dict
        
        