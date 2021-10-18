class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        
        if len(s) != len(t):
            return False
        
        s_dic = self.get_string_count(s)
        t_dic = self.get_string_count(t)
        
        return s_dic == t_dic
        
    
    
    
    
    
    
    def get_string_count(self, string):
        string_dic = {}
        for char in string:
            if char not in string_dic:
                string_dic[char] = 1
            else:
                string_dic[char] += 1
        return string_dic
                
        