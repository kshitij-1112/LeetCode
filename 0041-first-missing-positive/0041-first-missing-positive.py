class Solution:
    def firstMissingPositive(self, nums: list[int]) -> int:
        n = len(nums)
        
        for i in range(n):
            val = nums[i]
            # Cache nums[i] in 'val' to eliminate redundant array lookups
            while 1 <= val <= n and nums[val - 1] != val:
                dest = val - 1
                nums[i], nums[dest] = nums[dest], val
                val = nums[i]  # Update cached value for the next iteration
                
        for i in range(n):
            if nums[i] != i + 1:
                return i + 1
                
        return n + 1