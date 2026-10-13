class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        
        # Search Pruning: Count character frequencies on the board
        # If the last letter appears less often than the first letter, reverse the word
        # to start searching from the scarcer end, minimizing branch exploration.
        flat_board_chars = [char for row in board for char in row]
        if flat_board_chars.count(word[0]) > flat_board_chars.count(word[-1]):
            word = word[::-1]
            
        def dfs(r: int, c: int, k: int) -> bool:
            # Base case: matched the entire word
            if k == len(word):
                return True
            
            # Boundary checks, character mismatch, or already visited cell (marked as '#')
            if r < 0 or c < 0 or r >= m or c >= n or board[r][c] != word[k]:
                return False
            
            # Temporarily mark the current cell as visited in-place
            board[r][c] = '#'
            
            # Explore all 4 adjacent directions (Down, Up, Right, Left)
            found = (
                dfs(r + 1, c, k + 1) or
                dfs(r - 1, c, k + 1) or
                dfs(r, c + 1, k + 1) or
                dfs(r, c - 1, k + 1)
            )
            
            # Backtrack: Restore the original cell character
            board[r][c] = word[k]
            
            return found

        # Kick off DFS from every potential starting cell on the board
        for r in range(m):
            for c in range(n):
                if board[r][c] == word[0] and dfs(r, c, 0):
                    return True
                    
        return False  