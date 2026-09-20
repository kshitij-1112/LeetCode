class Solution:

  def solveSudoku(self, board: list[list[str]]) -> None:
    rows = [0] * 9
    cols = [0] * 9
    boxes = [0] * 9

    # 1. Initialize bitmasks for existing numbers
    for r in range(9):
      for c in range(9):
        val = board[r][c]
        if val != ".":
          bit = 1 << (int(val) - 1)
          rows[r] |= bit
          cols[c] |= bit
          boxes[(r // 3) * 3 + (c // 3)] |= bit

    def dfs() -> bool:
      min_choices = 10
      best_r, best_c = -1, -1
      best_candidates = 0

      # MRV Heuristic: Find the empty cell with the fewest available choices
      for r in range(9):
        for c in range(9):
          if board[r][c] == ".":
            box_idx = (r // 3) * 3 + (c // 3)
            # Available digits represented by bits (1 to 9 -> bits 0 to 8)
            avail = ~(rows[r] | cols[c] | boxes[box_idx]) & 0x1FF
            choices = avail.bit_count()  # Native C-optimized bit counter

            if choices == 0:
              return False  # Dead end found
            if choices < min_choices:
              min_choices = choices
              best_r, best_c = r, c
              best_candidates = avail
              if min_choices == 1:
                break  # Can't get fewer than 1 choice, optimal greediness
        if min_choices == 1:
          break

      # If no empty cells are left, the board is successfully solved
      if best_r == -1:
        return True

      box_idx = (best_r // 3) * 3 + (best_c // 3)
      candidates = best_candidates

      # Try each available digit using bit manipulation
      while candidates:
        bit = candidates & -candidates  # Extract lowest set bit
        candidates ^= bit
        num = bit.bit_length() - 1  # Convert bit to digit index (0-8)

        # Place the number
        rows[best_r] |= bit
        cols[best_c] |= bit
        boxes[box_idx] |= bit
        board[best_r][best_c] = chr(49 + num)

        if dfs():
          return True

        # Backtrack (undo changes)
        rows[best_r] &= ~bit
        cols[best_c] &= ~bit
        boxes[box_idx] &= ~bit
        board[best_r][best_c] = "."

      return False

    dfs()