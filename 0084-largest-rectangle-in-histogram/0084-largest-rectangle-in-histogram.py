class Solution:

  def largestRectangleArea(self, heights: list[int]) -> int:
    stack = []
    max_area = 0
    n = len(heights)

    # Loop up to n + 1 to handle a virtual height of 0 at the end,
    # which flushes out all remaining bars in the stack.
    for i in range(n + 1):
      h = heights[i] if i < n else 0

      while stack and heights[stack[-1]] > h:
        height = heights[stack.pop()]
        # If stack is empty, the width spans from index 0 to i
        width = i if not stack else i - stack[-1] - 1
        current_area = height * width
        if current_area > max_area:
          max_area = current_area

      stack.append(i)

    return max_area