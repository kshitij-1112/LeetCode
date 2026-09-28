class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1.0
        
        # Handle negative powers by taking the reciprocal of x and making n positive
        if n < 0:
            x = 1 / x
            n = -n
            
        res = 1.0
        current_product = x
        
        while n > 0:
            # If the current bit of n is 1, multiply the result by the current product
            if n & 1:
                res *= current_product
            
            # Square the product for the next bit position
            current_product *= current_product
            
            # Shift n right by 1 bit (equivalent to integer division by 2)
            n >>= 1
            
        return res