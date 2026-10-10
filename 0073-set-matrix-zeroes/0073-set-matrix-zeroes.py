class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m, n = len(matrix), len(matrix[0])
        col0 = 1  # Acts as a fast integer flag for the first column
        
        # Step 1: Evaluate and mark rows and columns using the matrix borders
        for i in range(m):
            if matrix[i][0] == 0:
                col0 = 0
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0
                    
        # Step 2: Update the inner matrix cells based on the markers
        for i in range(1, m):
            row_marker = matrix[i][0] == 0
            for j in range(1, n):
                if row_marker or matrix[0][j] == 0:
                    matrix[i][j] = 0
                    
        # Step 3: Zero out the first row if matrix[0][0] is 0
        if matrix[0][0] == 0:
            for j in range(1, n):
                matrix[0][j] = 0
                
        # Step 4: Zero out the first column using the col0 flag
        if col0 == 0:
            for i in range(m):
                matrix[i][0] = 0