class Solution:

  def totalNQueens(self, n: int) -> int:
    full_mask = (1 << n) - 1

    def backtrack(cols: int, diag1: int, diag2: int) -> int:
      # If all columns are filled, we found a valid configuration
      if cols == full_mask:
        return 1

      # Find available positions in the current row
      available = ~(cols | diag1 | diag2) & full_mask
      count = 0

      while available:
        # Extract the lowest set bit (rightmost available position)
        p = available & -available
        # Clear this bit from available positions
        available ^= p

        # Recurse to the next row and accumulate solutions
        count += backtrack(cols | p, (diag1 | p) << 1, (diag2 | p) >> 1)

      return count

    return backtrack(0, 0, 0)