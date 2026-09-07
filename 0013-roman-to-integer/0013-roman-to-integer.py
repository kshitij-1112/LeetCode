class Solution:
    def romanToInt(self, s: str) -> int:
        values = {
            'I': 1, 'V': 5, 'X': 10,
            'L': 50, 'C': 100, 'D': 500, 'M': 1000
        }

        ans = 0

        for a, b in zip(s, s[1:]):
            ans += -values[a] if values[a] < values[b] else values[a]

        return ans + values[s[-1]]
