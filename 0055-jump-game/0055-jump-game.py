class Solution:

  def canJump(self, nums: list[int]) -> bool:
    goal = len(nums) - 1

    # Traverse backwards from the second-to-last index to the first index
    for i in range(len(nums) - 2, -1, -1):
      if i + nums[i] >= goal:
        goal = i

    # If the goal has reached index 0, we can successfully jump to the end
    return goal == 0