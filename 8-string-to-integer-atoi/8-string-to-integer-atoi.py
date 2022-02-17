class Solution:
    def myAtoi(self, s: str) -> int:
        
        
        """
        
        split string 
        if list is empty return 0
        set str_num = [0]
        
        set sign from str_num[0]
        set starting index baed on sign 
        set max or min based on sign
        0x80000000 min 0x7fffffff max
        
        iterate thrugh len of str_num
        
        if char is not a digit break
        
        get ord number
        set num *= 10
        add to num or_num - 48 will get actual int
        
        if num > our limit set to num break frmo loop return sign min
        
        else return  num * sign
        
        """
        str_list = s.split()
        if not str_list:
            return 0
        str_num = str_list[0]
        
        num = 0
        sign = -1 if str_num[0] == '-' else +1
        start = 1 if str_num[0] in '-+' else 0
        limit = 0x80000000 if sign == -1 else 0x7fffffff
        
        for i in range(start, len(str_num)):
            if not str_num[i].isdigit():
                break
            
            ord_num = ord(str_num[i])
            num *=10
            num += ord_num - 48
            
            if num >= limit:
                num = limit
                break
        return sign * num