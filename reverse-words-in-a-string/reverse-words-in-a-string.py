class Solution:
    def reverseWords(self, s: str) -> str:
        
        s_reverse = s.split()
        s_reverse = s_reverse[::-1]
        answer = ""
        
        for word in s_reverse:
            answer += word + ' '
            
        answer = answer.rstrip(' ')
        return answer
        