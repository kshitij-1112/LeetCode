from typing import List


class Solution:

  def permuteUnique(self, nums: List[int]) -> List[List[int]]:
    nums.sort()  # Sort to group duplicates together
    res = []
    visited = [False] * len(nums)

    def backtrack(path: List[int]):
      if len(path) == len(nums):
        res.append(path[:])  # Append a copy of the valid permutation
        return

      for i in range(len(nums)):
        # If the element is already used, skip it
        if visited[i]:
          continue

        # Duplicate-skipping condition:
        # If current element is equal to the previous one, and the previous
        # one was NOT used in this recursive branch, skip it to avoid duplicates.
        if i > 0 and nums[i] == nums[i - 1] and not visited[i - 1]:
          continue

        # Choose
        visited[i] = True
        path.append(nums[i])

        # Explore
        backtrack(path)

        # Un-choose (Backtrack)
        path.pop()
        visited[i] = False

    backtrack([])
    return res