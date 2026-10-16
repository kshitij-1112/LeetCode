class Solution:

  def maximalRectangle(self, matrix: list[list[str]]) -> int:
    if not matrix or not matrix[0]:
      return 0

    cols = len(matrix[0])
    # Initialize heights with an extra slot at the end permanently set to 0.
    # This acts as our permanent sentinel, avoiding dynamic list resizing/mutations inside the loop.
    heights = [0] * (cols + 1)
    max_area = 0

    for row in matrix:
      # Update the histogram heights based on the current row
      for j in range(cols):
        if row[j] == "1":
          heights[j] += 1
        else:
          heights[j] = 0

      # Inline Monotonic Stack algorithm for Largest Rectangle in Histogram
      stack = []
      push = stack.append
      pop = stack.pop
      ans = 0

      for i, h in enumerate(heights):
        while stack and heights[stack[-1]] > h:
          height = heights[pop()]
          width = i if not stack else i - stack[-1] - 1
          current_area = height * width
          if current_area > ans:
            ans = current_area
        push(i)

      if ans > max_area:
        max_area = ans

    return max_area