class Solution:

  def largestRectangleArea(self, heights: list[int]) -> int:
    # 1. Append a sentinel 0 to flush out remaining elements automatically,
    # eliminating bounds-checking conditionals inside the loop.
    heights.append(0)

    stack = []
    ans = 0

    # Local binding to avoid dictionary/attribute lookup overhead in the loop
    append_stack = stack.append
    pop_stack = stack.pop

    for i, h in enumerate(heights):
      while stack and heights[stack[-1]] > h:
        height = heights[pop_stack()]
        width = i if not stack else i - stack[-1] - 1

        # Direct inline comparison is faster than calling max() repeatedly
        current_area = height * width
        if current_area > ans:
          ans = current_area

      append_stack(i)

    # Clean up the mutated list to leave input pristine
    heights.pop()
    return ans