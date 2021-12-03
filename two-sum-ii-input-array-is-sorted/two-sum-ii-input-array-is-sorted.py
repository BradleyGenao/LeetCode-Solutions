class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        
        differences = collections.defaultdict(int)
        res = []
        for i, num in enumerate(numbers):
            diffs = target - num
            if diffs in differences:
                res.append(differences[diffs] + 1)
                res.append(i + 1)
                
                return res
            differences[num] = i
                
        