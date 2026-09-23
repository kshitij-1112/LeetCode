class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"
            
        m, n = len(num1), len(num2)
        pos = [0] * (m + n)
        
        # Traverse both strings from right to left
        for i in range(m - 1, -1, -1):
            n1 = ord(num1[i]) - 48
            for j in range(n - 1, -1, -1):
                n2 = ord(num2[j]) - 48
                
                # Multiply digits and add to the existing carry/value position
                p1, p2 = i + j, i + j + 1
                total = n1 * n2 + pos[p2]
                
                pos[p2] = total % 10
                pos[p1] += total // 10
                
        # Convert array to string and strip leading zeros
        return "".join(map(str, pos)).lstrip("0")