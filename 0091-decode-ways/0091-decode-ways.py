class Solution:
    def numDecodings(self, s: str) -> int:
        if not s or s[0] == '0':
            return 0
        
        # dp_prev2 represents dp[i-2], dp_prev1 represents dp[i-1]
        dp_prev2 = 1
        dp_prev1 = 1
        
        for i in range(1, len(s)):
            current = 0
            
            # 1. Single-digit decoding (Valid if current char is not '0')
            if s[i] != '0':
                current += dp_prev1
                
            # 2. Two-digit decoding (Valid if formed number is between "10" and "26")
            prev_char, curr_char = s[i - 1], s[i]
            if prev_char == '1' or (prev_char == '2' and curr_char <= '6'):
                current += dp_prev2
                
            # If no valid decodings can be made, it's impossible to decode the string
            if current == 0:
                return 0
                
            # Shift pointers forward
            dp_prev2 = dp_prev1
            dp_prev1 = current
            
        return dp_prev1