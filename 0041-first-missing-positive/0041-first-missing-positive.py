class Solution:
    def firstMissingPositive(self, nums: list[int]) -> int:
        n = len(nums)
        has_one = False
        
        # Step 1: Check if 1 is present and clean up out-of-range numbers
        for i in range(n):
            if nums[i] == 1:
                has_one = True
            elif nums[i] <= 0 or nums[i] > n:
                nums[i] = 1
                
        # If 1 is missing anywhere in the array, the answer must be 1
        if not has_one:
            return 1
            
        # Step 2: Use array indices as hash keys by negating values at (val - 1)
        for i in range(n):
            idx = abs(nums[i]) - 1
            if nums[idx] > 0:
                nums[idx] = -nums[idx]
                
        # Step 3: Find the first index that remains positive
        for i in range(n):
            if nums[i] > 0:
                return i + 1
                
        # If all elements from 1 to n are marked, the answer is n + 1
        return n + 1