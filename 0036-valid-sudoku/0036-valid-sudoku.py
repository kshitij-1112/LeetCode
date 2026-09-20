class Solution:

  def isValidSudoku(self, board: list[list[str]]) -> bool:
    rows = [0] * 9
    cols = [0] * 9
    boxes = [0] * 9

    for r in range(9):
      for c in range(9):
        val = board[r][c]
        if val == ".":
          continue

        # Convert '1'-'9' to a bit position (0 to 8)
        bit = 1 << (ord(val) - 49)  # ord('1') is 49
        box_idx = (r // 3) * 3 + (c // 3)

        # Check if the bit is already set (duplicate found)
        if (rows[r] & bit) or (cols[c] & bit) or (boxes[box_idx] & bit):
          return False

        # Set the bit
        rows[r] |= bit
        cols[c] |= bit
        boxes[box_idx] |= bit

    return True