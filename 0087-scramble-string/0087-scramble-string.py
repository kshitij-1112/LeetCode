from functools import cache

class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        @cache
        def dfs(i: int, j: int, k: int) -> bool:
            # Base case: length 1 comparison
            if k == 1:
                return s1[i] == s2[j]
            
            # Fast-path: if the substrings are already identical, they match
            if s1[i:i + k] == s2[j:j + k]:
                return True
                
            # Try all possible split positions 'h'
            for h in range(1, k):
                # Case 1: Non-swapped (left-left, right-right)
                if dfs(i, j, h) and dfs(i + h, j + h, k - h):
                    return True
                
                # Case 2: Swapped (left-right, right-left)
                if dfs(i, j + k - h, h) and dfs(i + h, j, k - h):
                    return True
                    
            return False

        return dfs(0, 0, len(s1))