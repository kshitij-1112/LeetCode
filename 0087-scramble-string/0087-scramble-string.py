
from functools import lru_cache

class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        n = len(s1)

        if s1 == s2:
            return True

        # Pack character counts into 5-bit fields.
        # n <= 30, so each character count fits in 5 bits.
        bits = [1 << (5 * i) for i in range(26)]

        p1 = [0] * (n + 1)
        p2 = [0] * (n + 1)

        for i in range(n):
            p1[i + 1] = p1[i] + bits[ord(s1[i]) - 97]
            p2[i + 1] = p2[i] + bits[ord(s2[i]) - 97]

        @lru_cache(None)
        def dfs(i: int, j: int, length: int) -> bool:
            if s1[i:i + length] == s2[j:j + length]:
                return True

            sig1 = p1[i + length] - p1[i]
            sig2 = p2[j + length] - p2[j]

            if sig1 != sig2:
                return False

            for k in range(1, length):
                left = p1[i + k] - p1[i]

                # No swap: left part matches left part
                if left == p2[j + k] - p2[j]:
                    if (dfs(i, j, k) and
                        dfs(i + k, j + k, length - k)):
                        return True

                # Swap: left part matches right part
                if left == p2[j + length] - p2[j + length - k]:
                    if (dfs(i, j + length - k, k) and
                        dfs(i + k, j, length - k)):
                        return True

            return False

        return dfs(0, 0, n)
