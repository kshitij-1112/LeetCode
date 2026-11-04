class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        m, n = len(s), len(t)
        
        # Early exit if target is longer than source
        if n > m:
            return 0
            
        # dp[j] represents the number of distinct subsequences of s prefix matching t[:j]
        dp = [0] * (n + 1)
        dp[0] = 1
        
        for i in range(1, m + 1):
            s_char = s[i - 1]
            # Optimization: only loop up to the minimum of what's possible 
            # to match current length i or total length n.
            end_j = min(i, n)
            
            for j in range(end_j, 0, -1):
                if s_char == t[j - 1]:
                    dp[j] += dp[j - 1]
                    
        return dp[n]