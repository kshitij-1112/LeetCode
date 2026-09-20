class Solution:

  def solveSudoku(self, board: list[list[str]]) -> None:
    rows = [0] * 9
    cols = [0] * 9
    boxes = [0] * 9
    empty_cells = []

    # 1. Initialize tracking bitmasks and find all empty cells
    for r in range(9):
      for c in range(9):
        val = board[r][c]
        if val == ".":
          empty_cells.append((r, c))
        else:
          bit = 1 << (ord(val) - 49)
          box_idx = (r // 3) * 3 + (c // 3)
          rows[r] |= bit
          cols[c] |= bit
          boxes[box_idx] |= bit

    # 2. Backtracking DFS with index tracking
    def backtrack(idx: int) -> bool:
      if idx == len(empty_cells):
        return True  # All empty cells filled successfully

      r, c = empty_cells[idx]
      box_idx = (r // 3) * 3 + (c // 3)

      # Try digits 1 through 9 represented by bits 0 to 8
      for i in range(9):
        bit = 1 << i
        # Check if digit is already used in row, col, or box
        if not (rows[r] & bit) and not (cols[c] & bit) and not (boxes[box_idx] & bit):
          # Place the digit
          rows[r] |= bit
          cols[c] |= bit
          boxes[box_idx] |= bit
          board[r][c] = chr(49 + i)

          # Recurse to the next empty cell
          if backtrack(idx + 1):
            return True

          # Backtrack (undo changes)
          rows[r] &= ~bit
          cols[c] &= ~bit
          boxes[box_idx] &= ~bit
          board[r][c] = "."

      return False

    backtrack(0)