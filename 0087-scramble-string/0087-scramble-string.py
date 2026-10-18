class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        if len(s1) != len(s2):
            return False
        if s1 == s2:
            return True
            
        n = len(s1)
        # dp[length][i1][i2] stores whether s1[i1 : i1+length] 
        # can scramble to s2[i2 : i2+length]
        dp = [[[False] * n for _ in range(n)] for _ in range(n + 1)]
        
        # Base Case: Substrings of length 1
        for i1 in range(n):
            for i2 in range(n):
                dp[1][i1][i2] = (s1[i1] == s2[i2])
                
        # Iterate over all possible lengths from 2 to n
        for length in range(2, n + 1):
            for i1 in range(n - length + 1):
                for i2 in range(n - length + 1):
                    # Try every possible split point 'k'
                    for k in range(1, length):
                        # Case 1: Non-swapped condition
                        if dp[k][i1][i2] and dp[length - k][i1 + k][i2 + k]:
                            dp[length][i1][i2] = True
                            break
                        # Case 2: Swapped condition
                        if dp[k][i1][i2 + length - k] and dp[length - k][i1 + k][i2]:
                            dp[length][i1][i2] = True
                            break
                            
        return dp[n][0][0]