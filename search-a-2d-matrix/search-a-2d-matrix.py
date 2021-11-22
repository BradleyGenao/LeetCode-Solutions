class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        left, right = 0, m*n - 1
        while left < right:
            mid = left + (right - left) // 2
            if matrix[mid // n][ mid % n] >= target:
                right = mid
            else:
                left = mid + 1
        return matrix[left // n][left % n] == target

        
        
        