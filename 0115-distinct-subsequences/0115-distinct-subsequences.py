class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        m, n = len(s), len(t)
        
        # dp[j] represents the number of distinct subsequences of s[:i] that equal t[:j]
        # We only need a 1D array of size n + 1
        dp = [0] * (n + 1)
        
        # An empty string t can always be formed by an empty prefix of s in 1 way
        dp[0] = 1
        
        for i in range(1, m + 1):
            # We iterate backwards to avoid overwriting values needed from the previous row
            for j in range(n, 0, -1):
                if s[i - 1] == t[j - 1]:
                    dp[j] += dp[j - 1]
                    
        return dp[n]