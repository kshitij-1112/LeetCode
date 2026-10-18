
class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        n = len(s1)

        if s1 == s2:
            return True

        # Encode character frequencies in 5-bit fields.
        # Each character occurs at most 30 times.
        bits = [1 << (5 * i) for i in range(26)]

        p1 = [0] * (n + 1)
        p2 = [0] * (n + 1)

        for i in range(n):
            p1[i + 1] = p1[i] + bits[ord(s1[i]) - 97]
            p2[i + 1] = p2[i] + bits[ord(s2[i]) - 97]

        # dp[length][i][j]:
        # s1[i:i+length] is a scramble of s2[j:j+length]
        dp = [[[False] * n for _ in range(n)]
              for _ in range(n + 1)]

        # Base case: substrings of length 1
        for i in range(n):
            for j in range(n):
                dp[1][i][j] = s1[i] == s2[j]

        for length in range(2, n + 1):
            limit = n - length + 1

            for i in range(limit):
                sig1 = p1[i + length] - p1[i]

                for j in range(limit):
                    # O(1) character-frequency check
                    if sig1 != p2[j + length] - p2[j]:
                        continue

                    # Identical substrings need no splitting
                    if s1[i:i + length] == s2[j:j + length]:
                        dp[length][i][j] = True
                        continue

                    for k in range(1, length):
                        # No swap
                        if (dp[k][i][j] and
                            dp[length - k][i + k][j + k]):
                            dp[length][i][j] = True
                            break

                        # Swap
                        if (dp[k][i][j + length - k] and
                            dp[length - k][i + k][j]):
                            dp[length][i][j] = True
                            break

        return dp[n][0][0]
