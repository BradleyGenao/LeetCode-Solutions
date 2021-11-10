class Solution:
    def isValid(self, s: str) -> bool:
        
        """
        
        using a stack 
        iterate through the list when a ( [ { is found add to stack
        check stack is not empaty return false
        
        if char == closing 
        pop stack if pop is not opening return false
        
        at the end check if the stack is empty return true
        
        """
        
        stack = []
        for char in s:
            if char == '(' or char == '[' or char == '{':
                stack.append(char)
            if len(stack) == 0:
                return False
            if char == ')':
                z = stack.pop()
                if z != '(':
                    return False
            if char == '}':
                z = stack.pop()
                if z != '{':
                    return False
            if char == ']':
                z = stack.pop()
                if z != '[':
                    return False
        if len(stack) == 0:
            return True
        else:
            return False