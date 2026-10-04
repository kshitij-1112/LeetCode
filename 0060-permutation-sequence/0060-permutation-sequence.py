import math

class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        # Convert k to 0-indexed for easier modulo arithmetic
        k -= 1
        
        # Create a list of available numbers
        numbers = list(range(1, n + 1))
        
        # Calculate (n - 1)!
        factorial = math.factorial(n - 1)
        
        permutation = []
        
        for i in range(n, 0, -1):
            # Find the index of the current digit
            index = k // factorial
            permutation.append(str(numbers.pop(index)))
            
            # Update k and the factorial for the next position
            if i > 1:
                k %= factorial
                factorial //= (i - 1)
                
        return "".join(permutation)