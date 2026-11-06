class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        triangle = []
        for i in range(numRows):
            # Pre-fill the row with 1s (handles the 1st and last elements automatically)
            row = [1] * (i + 1)
            
            # Calculate intermediate values using the previous row
            for j in range(1, i):
                row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
                
            triangle.append(row)
            
        return triangle