class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        
        first_row_has_zero, first_col_has_zero = False, False
        m, n = len(matrix), len(matrix[0])

        for j in range(n):
            first_row_has_zero = first_row_has_zero or (matrix[0][j] == 0)

        for i in range(m):
            first_col_has_zero = first_col_has_zero or (matrix[i][0] == 0)
            for j in range(0, n):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0

        #print(matrix, first_row_has_zero, first_col_has_zero)

        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
        
        #print(matrix)
        if first_row_has_zero:
            for j in range(n):
                matrix[0][j] = 0
        
        if first_col_has_zero:
            for i in range(m):
                matrix[i][0] = 0