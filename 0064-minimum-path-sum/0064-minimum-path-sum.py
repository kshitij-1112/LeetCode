class Solution:

  def minPathSum(self, grid: list[list[int]]) -> int:
    m, n = len(grid), len(grid[0])

    # Pre-optimize the first row
    row0 = grid[0]
    for j in range(1, n):
      row0[j] += row0[j - 1]

    # Traverse remaining rows with cached row references
    for i in range(1, m):
      prev_row = grid[i - 1]
      curr_row = grid[i]

      # Handle first column of the current row
      curr_row[0] += prev_row[0]

      # Inner loop optimized with local variable caching
      for j in range(1, n):
        curr_row[j] += (
            prev_row[j] if prev_row[j] < curr_row[j - 1] else curr_row[j - 1]
        )

    return grid[-1][-1]