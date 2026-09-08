class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        strs.sort()
        a, b = strs[0], strs[-1]

        i = 0
        while i < len(a) and i < len(b) and a[i] == b[i]:
            i += 1

        return a[:i]
