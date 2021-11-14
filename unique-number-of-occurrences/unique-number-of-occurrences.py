class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        
        """
        [1,2,2,3,3,3] = True
        [1,2,3,4,5] = False
        
        Linear Time Best Case
        
        Step 1: Iterate through array adding to count[value] = count could also use Counter
        
        Step 2: add a unique check dic and add the values to it and break if it is seen
        
        
        
        """
        
        unique = collections.defaultdict(int)
        checker = {}
        for num in arr:
            unique[num] +=1
        for key, value in unique.items():
            if checker.get(value):
                return False
            else:
                checker[value] = True
        print(checker.get(1))   
        return True 
            
        
                
        