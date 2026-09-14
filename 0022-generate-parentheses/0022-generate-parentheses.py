class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        ans = []
        path = [''] * (2 * n)

        def dfs(i: int, open: int, close: int) -> None:
            if i == 2 * n:
                ans.append(''.join(path))
                return

            if open < n:
                path[i] = '('
                dfs(i + 1, open + 1, close)

            if close < open:
                path[i] = ')'
                dfs(i + 1, open, close + 1)

        dfs(0, 0, 0)
        return ans