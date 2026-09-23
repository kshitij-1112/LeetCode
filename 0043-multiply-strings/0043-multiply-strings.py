class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"
            
        m, n = len(num1), len(num2)
        res = [0] * (m + n)
        
        for i in range(m - 1, -1, -1):
            d1 = ord(num1[i]) - 48
            for j in range(n - 1, -1, -1):
                total = d1 * (ord(num2[j]) - 48) + res[i + j + 1]
                res[i + j + 1] = total % 10
                res[i + j] += total // 10
                
        # Skip leading zeros without creating extra intermediate lists
        start = 0
        while start < m + n and res[start] == 0:
            start += 1
            
        # Fast character conversion using chr() instead of map(str, ...)
        return "".join(chr(x + 48) for x in res[start:])