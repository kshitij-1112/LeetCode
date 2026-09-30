from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cur = res = nums[0]
        
        for x in nums[1:]:
            if cur < 0:
                cur = x
            else:
                cur += x
                
            if cur > res:
                res = cur
                
        return res