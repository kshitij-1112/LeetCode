class Solution:
    def firstMissingPositive(self, nums: list[int]) -> int:
        n = len(nums)
        
        # Step 1: Replace numbers out of the range [1, n] with a placeholder (n + 1)
        # Because the answer must be between 1 and n + 1.
        for i in range(n):
            if nums[i] <= 0 or nums[i] > n:
                nums[i] = n + 1
                
        # Step 2: Use index as a hash key by marking the presence of numbers
        # by making the value at index (val - 1) negative.
        for i in range(n):
            val = abs(nums[i])
            if 1 <= val <= n:
                if nums[val - 1] > 0:
                    nums[val - 1] = -nums[val - 1]
                    
        # Step 3: Find the first index with a positive value
        for i in range(n):
            if nums[i] > 0:
                return i + 1
                
        # If all numbers from 1 to n are present, the answer is n + 1
        return n + 1