import collections

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        
         anagram_dict = defaultdict(list)
        
         for string in strs:
                anagram_dict[str(sorted(string))].append(string)
        
         return anagram_dict.values()
    
        