class Solution:

  def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
    if not matrix:
      return False

    m = len(matrix)
    n = len(matrix[0])
    left = 0
    right = m * n - 1

    while left <= right:
      mid = (left + right) // 2
      # Avoids tuple allocation by using direct arithmetic instead of divmod()
      row = mid // n
      col = mid % n
      val = matrix[row][col]

      if val == target:
        return True
      elif val < target:
        left = mid + 1
      else:
        right = mid - 1

    return False