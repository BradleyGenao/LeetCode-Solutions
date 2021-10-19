class Solution:
    def reverse(self, x: int) -> int:
        
        
        
        
        
        if x == 0:
            return 0
        negative = False
        
        
        reverse_x = str(x)[::-1]
        if reverse_x[-1] == '-':
            negative = True
            reverse_x = reverse_x[:len(reverse_x) -1 ]
            
        
        
            
        
        
        index = 0 
        
        
                
       
        while '0' == reverse_x[0]:
            reverse_x= reverse_x[index+1:]
            
        
        if int(reverse_x)  <  -2 **-31 or int(reverse_x) > (2 ** 31) -1:
            return 0
        
        if negative:
            return '-' + reverse_x
        else:
            return reverse_x