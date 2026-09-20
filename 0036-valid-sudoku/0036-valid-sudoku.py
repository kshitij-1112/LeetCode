class Solution:

  def isValidSudoku(self, board: list[list[str]]) -> bool:
    # Pre-allocate 9x9 tracking matrices for rows, columns, and 3x3 boxes
    rows = [[False] * 9 for _ in range(9)]
    cols = [[False] * 9 for _ in range(9)]
    boxes = [[False] * 9 for _ in range(9)]

    for r in range(9):
      for c in range(9):
        val = board[r][c]
        if val == ".":
          continue

        # Convert character '1'-'9' to index 0-8
        num = int(val) - 1
        box_idx = (r // 3) * 3 + (c // 3)

        # If already marked true, a duplicate exists
        if rows[r][num] or cols[c][num] or boxes[box_idx][num]:
          return False

        # Mark as seen
        rows[r][num] = True
        cols[c][num] = True
        boxes[box_idx][num] = True

    return True