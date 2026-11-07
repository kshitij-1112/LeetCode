from typing import List

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        # Traverse backwards from the second-to-last row up to the top row
        for i in range(len(triangle) - 2, -1, -1):
            row_i = triangle[i]
            next_row = triangle[i + 1]
            for j in range(len(row_i)):
                # Add the minimum of the two adjacent numbers in the row below
                row_i[j] += min(next_row[j], next_row[j + 1])
                
        # The top element now holds the minimum path sum
        return triangle[0][0]