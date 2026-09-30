from typing import List

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix or not matrix[0]:
            return []
            
        m, n = len(matrix), len(matrix[0])
        # Preallocate exact memory to prevent dynamic resizing/fragmentation
        res = [0] * (m * n)
        idx = 0
        
        top, bottom = 0, m - 1
        left, right = 0, n - 1
        
        while top <= bottom and left <= right:
            # 1. Traverse Right
            for col in range(left, right + 1):
                res[idx] = matrix[top][col]
                idx += 1
            top += 1
            
            # 2. Traverse Down
            for row in range(top, bottom + 1):
                res[idx] = matrix[row][right]
                idx += 1
            right -= 1
            
            # 3. Traverse Left
            if top <= bottom:
                for col in range(right, left - 1, -1):
                    res[idx] = matrix[bottom][col]
                    idx += 1
                bottom -= 1
                
            # 4. Traverse Up
            if left <= right:
                for row in range(bottom, top - 1, -1):
                    res[idx] = matrix[row][left]
                    idx += 1
                left += 1
                
        return res