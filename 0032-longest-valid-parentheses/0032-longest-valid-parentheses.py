class Solution:
    def longestValidParentheses(self, s: str) -> int:
        max_len = 0
        left = right = 0
        
        # 1. Left to Right Pass
        for char in s:
            if char == '(':
                left += 1
            else:
                right += 1
                
            if left == right:
                max_len = max(max_len, 2 * right)
            elif right > left:
                # Invalid sequence, reset counts
                left = right = 0
                
        left = right = 0
        
        # 2. Right to Left Pass (catches cases like "(()")
        for char in reversed(s):
            if char == '(':
                left += 1
            else:
                right += 1
                
            if left == right:
                max_len = max(max_len, 2 * left)
            elif left > right:
                # Invalid sequence, reset counts
                left = right = 0
                
        return max_len