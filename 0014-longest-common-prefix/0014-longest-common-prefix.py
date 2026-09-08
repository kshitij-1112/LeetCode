class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        prefix = strs[0]

        for s in strs[1:]:
            i = 0

            # Find how much of prefix matches s
            while i < len(prefix) and i < len(s) and prefix[i] == s[i]:
                i += 1

            prefix = prefix[:i]

            # No common prefix
            if not prefix:
                return ""

        return prefix
