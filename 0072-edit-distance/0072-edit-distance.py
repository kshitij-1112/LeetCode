class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # Ensure word1 is the longer string and word2 is the shorter one
        # to minimize the size of our rolling DP array (O(min(m, n)) space).
        if len(word1) < len(word2):
            word1, word2 = word2, word1
            
        m, n = len(word1), len(word2)
        
        # Initialize the dp array for the base cases (converting empty string to word2)
        prev = list(range(n + 1))
        
        for i in range(1, m + 1):
            curr = [i] + [0] * n
            for j in range(1, n + 1):
                if word1[i - 1] == word2[j - 1]:
                    curr[j] = prev[j - 1]
                else:
                    curr[j] = 1 + min(
                        prev[j],     # Delete
                        curr[j - 1], # Insert
                        prev[j - 1]  # Replace
                    )
            prev = curr
            
        return prev[n]