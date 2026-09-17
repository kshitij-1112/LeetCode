class Solution:

  def nextPermutation(self, nums: list[int]) -> None:
    """Do not return anything, modify nums in-place instead."""
    n = len(nums)

    # Step 1: Find the first element from the right that is smaller than the one after it (pivot)
    i = n - 2
    while i >= 0 and nums[i] >= nums[i + 1]:
      i -= 1

    # Step 2: If such a pivot is found
    if i >= 0:
      # Find the smallest element to the right of 'i' that is greater than nums[i]
      j = n - 1
      while nums[j] <= nums[i]:
        j -= 1
      # Swap them
      nums[i], nums[j] = nums[j], nums[i]

    # Step 3: Reverse the suffix starting from i + 1 to get the smallest lexicographical order
    left, right = i + 1, n - 1
    while left < right:
      nums[left], nums[right] = nums[right], nums[left]
      left += 1
      right -= 1