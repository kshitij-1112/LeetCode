class Solution:
    def firstMissingPositive(self, nums: list[int]) -> int:
        n = len(nums)
        
        # Pass 1: Neutralize numbers out of the valid range [1, n] by setting them to n + 1
        for i in range(n):
            x = nums[i]
            if x <= 0 or x > n:
                nums[i] = n + 1
                
        # Pass 2: Mark presence by negating the value at the target index
        for i in range(n):
            x = nums[i]
            # Fast absolute value without calling built-in abs() function
            if x < 0:
                x = -x
            if x <= n:
                idx = x - 1
                if nums[idx] > 0:
                    nums[idx] = -nums[idx]
                    
        # Pass 3: Find the first index that remains positive
        for i in range(n):
            if nums[i] > 0:
                return i + 1
                
        return n + 1