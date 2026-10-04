class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        # Precomputed factorials up to 9! to completely bypass math library/loop overhead
        factorials = [1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880]
        
        # Convert k to 0-indexed
        k -= 1
        
        # Available numbers as characters to avoid conversion inside the loop
        nums = [str(i) for i in range(1, n + 1)]
        res = []
        
        for i in range(n, 0, -1):
            fact = factorials[i - 1]
            index = k // fact
            res.append(nums.pop(index))
            k %= fact
            
        return "".join(res)