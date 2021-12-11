class NumArray:

    def __init__(self, nums: List[int]):
        
        self.sum_arr = nums
        for i in range( len(nums)- 1):
            self.sum_arr[i+1] += self.sum_arr[i]
        

    def sumRange(self, left: int, right: int) -> int:
        if left == 0:
            return self.sum_arr[right]
        return self.sum_arr[right] - self.sum_arr[left- 1]
        
       
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)