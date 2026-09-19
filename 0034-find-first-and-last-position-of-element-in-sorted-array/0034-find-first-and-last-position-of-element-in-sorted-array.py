from bisect import bisect_left, bisect_right
from typing import List

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # Find the starting index using bisect_left
        left = bisect_left(nums, target)
        
        # Check if the target actually exists in the array
        if left == len(nums) or nums[left] != target:
            return [-1, -1]
        
        # Find the ending index using bisect_right (minus 1 because bisect_right 
        # gives the insertion point after the rightmost target)
        right = bisect_right(nums, target) - 1
        
        return [left, right]