import functools
from collections import Counter

class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        # Fast memoized recursive helper function
        @functools.cache
        def dp(sub1: str, sub2: str) -> bool:
            # Base Cases
            if sub1 == sub2:
                return True
            # Pruning: If character frequencies do not match, they can never be scrambles
            if Counter(sub1) != Counter(sub2):
                return False
            
            n = len(sub1)
            # Try every possible split position 'i'
            for i in range(1, n):
                # Case 1: No Swap (left matches left, right matches right)
                if dp(sub1[:i], sub2[:i]) and dp(sub1[i:], sub2[i:]):
                    return True
                
                # Case 2: Swap (left matches right, right matches left)
                if dp(sub1[:i], sub2[n-i:]) and dp(sub1[i:], sub2[:n-i]):
                    return True
                    
            return False

        return dp(s1, s2)