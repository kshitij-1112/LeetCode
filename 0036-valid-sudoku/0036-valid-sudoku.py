class Solution:

  def isValidSudoku(self, board: list[list[str]]) -> bool:
    seen = set()

    for r in range(9):
      for c in range(9):
        val = board[r][c]
        if val == ".":
          continue

        # Create unique string identifiers for row, column, and 3x3 sub-box
        row_id = f"row {r}: {val}"
        col_id = f"col {c}: {val}"
        box_id = f"box {r // 3},{c // 3}: {val}"

        # If any identifier already exists, the board is invalid
        if row_id in seen or col_id in seen or box_id in seen:
          return False

        seen.add(row_id)
        seen.add(col_id)
        seen.add(box_id)

    return True