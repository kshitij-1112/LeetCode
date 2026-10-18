from collections import Counter
import functools

class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        @functools.cache
        def dfs(i1: int, i2: int, length: int) -> bool:
            # Base Case: Single character comparison
            if length == 1:
                return s1[i1] == s2[i2]
            
            sub1 = s1[i1:i1 + length]
            sub2 = s2[i2:i2 + length]
            
            # Direct match check
            if sub1 == sub2:
                return True
                
            # Fast Anagram Pruning (avoids expanding dead paths)
            if Counter(sub1) != Counter(sub2):
                return False
                
            # Try all possible split positions
            for k in range(1, length):
                # Case 1: Non-swapped 
                if dfs(i1, i2, k) and dfs(i1 + k, i2 + k, length - k):
                    return True
                # Case 2: Swapped
                if dfs(i1, i2 + length - k, k) and dfs(i1 + k, i2, length - k):
                    return True
                    
            return False

        return dfs(0, 0, len(s1))