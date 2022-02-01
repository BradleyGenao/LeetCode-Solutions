class Solution:
    def isValid(self, s: str) -> bool:
        
        
        opening = {'(', '{', '['}
        closed = {')': '(', ']' : '[', '}' : '{' }
        stack = []
        
        for char in s:
            if char in opening:
                stack.append(char)
            elif not stack:
                return False
            elif char in closed:
                top_stack = stack.pop()
                if closed[char] != top_stack:
                    return False
        return not stack
        
        
        