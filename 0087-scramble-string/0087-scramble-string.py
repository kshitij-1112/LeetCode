
from functools import lru_cache
from collections import Counter

class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        n = len(s1)

        if s1 == s2:
            return True

        if Counter(s1) != Counter(s2):
            return False

        @lru_cache(None)
        def dfs(i: int, j: int, length: int) -> bool:
            a = s1[i:i + length]
            b = s2[j:j + length]

            if a == b:
                return True

            if Counter(a) != Counter(b):
                return False

            for k in range(1, length):
                # No swap
                if (dfs(i, j, k) and
                    dfs(i + k, j + k, length - k)):
                    return True

                # Swap
                if (dfs(i, j + length - k, k) and
                    dfs(i + k, j, length - k)):
                    return True

            return False

        return dfs(0, 0, n)
