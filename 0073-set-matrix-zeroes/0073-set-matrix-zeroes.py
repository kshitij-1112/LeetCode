class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m, n = len(matrix), len(matrix[0])
        is_col = False  # Flag to track if the first column should be zeroed
        
        # Step 1: Mark zeroes in the first row and first column
        for i in range(m):
            if matrix[i][0] == 0:
                is_col = True
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0
                    
        # Step 2: Use markers to set elements to zero (excluding first row/col)
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
                    
        # Step 3: Handle the first row based on matrix[0][0]
        if matrix[0][0] == 0:
            for j in range(n):
                matrix[0][j] = 0
                
        # Step 4: Handle the first column based on is_col flag
        if is_col:
            for i in range(m):
                matrix[i][0] = 0