class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        # Define 32-bit signed integer limits
        INT_MIN, INT_MAX = -2**31, 2**31 - 1
        
        # Handle the special overflow case
        if dividend == INT_MIN and divisor == -1:
            return INT_MAX
        
        # Determine the sign of the result
        negative = (dividend < 0) != (divisor < 0)
        
        # Work with positive absolute values
        a, b = abs(dividend), abs(divisor)
        quotient = 0
        
        # Subtract powers of 2 multiples of divisor
        while a >= b:
            temp, multiple = b, 1
            # Double the temp and multiple as long as it fits into the remaining dividend
            while a >= (temp << 1):
                temp <<= 1
                multiple <<= 1
            
            a -= temp
            quotient += multiple
            
        # Apply sign and ensure the result stays within 32-bit bounds
        result = -quotient if negative else quotient
        return max(INT_MIN, min(result, INT_MAX))