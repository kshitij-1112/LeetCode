class Solution:
    def longestPalindrome(self, s: str) -> str:
        """
        Find the longest palindromic substring using dynamic programming.
      
        Args:
            s: Input string
          
        Returns:
            The longest palindromic substring
        """
        n = len(s)
      
        # dp[i][j] represents whether substring s[i:j+1] is a palindrome
        # Initialize all single characters as palindromes (True)
        dp = [[True] * n for _ in range(n)]
      
        # Variables to track the starting position and length of longest palindrome
        start_pos = 0
        max_length = 1
      
        # Fill the dp table bottom-up (from longer indices to shorter)
        for i in range(n - 2, -1, -1):
            for j in range(i + 1, n):
                # Initially mark as False for substrings with length > 1
                dp[i][j] = False
              
                # Check if characters at both ends match
                if s[i] == s[j]:
                    # For substrings of length 2: just check if ends match
                    # For longer substrings: also check if inner substring is palindrome
                    dp[i][j] = dp[i + 1][j - 1]
                  
                    # Update longest palindrome if current one is longer
                    if dp[i][j] and max_length < j - i + 1:
                        start_pos = i
                        max_length = j - i + 1
      
        # Return the longest palindromic substring
        return s[start_pos : start_pos + max_length]
