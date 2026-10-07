class Solution:

  def plusOne(self, digits: List[int]) -> List[int]:
    # Traverse the array from right to left (least to most significant digit)
    for i in range(len(digits) - 1, -1, -1):
      # If the current digit is less than 9, just increment it and return immediately
      if digits[i] < 9:
        digits[i] += 1
        return digits
      # If it's 9, it becomes 0, and the carry moves to the next left digit
      digits[i] = 0

    # If all digits were 9 (e.g., [9, 9] -> [0, 0]), we need an extra 1 at the beginning
    return [1] + digits