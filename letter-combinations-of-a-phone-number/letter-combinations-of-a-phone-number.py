class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        letters = {"2": "abc" , "3": "def" ,"4": "ghi" ,"5": "jkl" ,"6": "mno" ,"7": "pqrs" ,"8": "tuv" ,"9": "wxyz" }
        
        
        
        
        def dfs(index, path):
            if len(digits) == index:
                res.append(path)
                return 
            string1 = letters[digits[index]]
            for char in string1:
                dfs(index + 1, path + char)
        
        
        res = []
        if len(digits) < 1:
            return res
        
        dfs( 0, '')
        
        return res
        