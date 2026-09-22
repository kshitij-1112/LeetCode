class Solution:
    def firstMissingPositive(self, nums: list[int]) -> int:
        n = len(nums)
        
        # Step 1: Cyclic Sort — place each number x in its correct index (x - 1)
        for i in range(n):
            while 1 <= nums[i] <= n and nums[nums[i] - 1] != nums[i]:
                # Swap nums[i] with the element at its target destination
                correct_idx = nums[i] - 1
                nums[i], nums[correct_idx] = nums[correct_idx], nums[i]
                
        # Step 2: Find the first index where the number doesn't match index + 1
        for i in range(n):
            if nums[i] != i + 1:
                return i + 1
                
        # If all positions from 1 to n are correct, the answer is n + 1
        return n + 1