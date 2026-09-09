class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        if not digits:
            return []

        phone = (
            "", "", "abc", "def",
            "ghi", "jkl", "mno",
            "pqrs", "tuv", "wxyz"
        )

        result = [""]

        for d in digits:
            letters = phone[ord(d) - 48]
            result = [prefix + c for prefix in result for c in letters]

        return result

