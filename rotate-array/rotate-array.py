class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        
        k = k % len(nums)
        start = 0 
        count = 0
        while count < len(nums):
            current = start
            prev = nums[start]
            
            while True:
                nxt = (current + k) % len(nums)
                temp = nums[nxt]
                nums[nxt] = prev
                prev = temp
                current = nxt
                count +=1
                if start == current:
                    break 
            start+=1