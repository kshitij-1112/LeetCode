class Solution:

  def solveNQueens(self, n: int) -> List[List[str]]:
    res = []
    full_mask = (1 << n) - 1

    def backtrack(row: int, cols: int, diag1: int, diag2: int, state: list):
      if row == n:
        # Construct the board configuration only when a valid solution is found
        res.append(['.' * c + 'Q' + '.' * (n - 1 - c) for c in state])
        return

      # Find all available positions in the current row using bitwise operations
      available = ~(cols | diag1 | diag2) & full_mask

      while available:
        # Extract the lowest set bit (rightmost available position)
        p = available & -available
        # Clear this bit from available positions to mark it as visited
        available ^= p

        # Get the column index from the bit position
        col = p.bit_length() - 1

        state.append(col)
        # Recurse to the next row, shifting diagonals accordingly
        backtrack(row + 1, cols | p, (diag1 | p) << 1, (diag2 | p) >> 1, state)
        state.pop()

    backtrack(0, 0, 0, 0, [])
    return res