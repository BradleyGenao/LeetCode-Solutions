class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        
        
        rows = len(matrix)
        cols = len(matrix[0])
        row_zeroes = []
        col_zeroes = []
        
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == 0:
                    row_zeroes.append(i)
                    col_zeroes.append(j)
        
        for row in range(rows):
            if row in row_zeroes:
                matrix[row] = [0] * cols
            else:
                for col in col_zeroes:
                    matrix[row][col] = 0
        
        