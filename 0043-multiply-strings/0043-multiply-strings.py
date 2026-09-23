class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"
            
        m, n = len(num1), len(num2)
        pos = [0] * (m + n)
        
        # Phase 1: Accumulate raw cross-products (no carry handling inside)
        for i in range(m - 1, -1, -1):
            a = ord(num1[i]) - 48
            for j in range(n - 1, -1, -1):
                pos[i + j + 1] += a * (ord(num2[j]) - 48)
                
        # Phase 2: Single-pass carry propagation from right to left
        for i in range(m + n - 1, 0, -1):
            pos[i - 1] += pos[i] // 10
            pos[i] %= 10
            
        # Phase 3: Fast string construction (skipping leading zero)
        start = 0 if pos[0] != 0 else 1
        return "".join(chr(x + 48) for x in pos[start:])