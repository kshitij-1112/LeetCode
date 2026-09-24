class Solution:
    def jump(self, nums: list[int]) -> int:
        n = len(nums)
        if n <= 1:
            return 0
            
        jumps = 0
        current_end = 0
        farthest = 0
        
        # Traverse up to n - 1 to avoid unnecessary jump from the final index
        for i in range(n - 1):
            # Micro-optimization: explicit conditional is faster than built-in max() in Python loops
            temp = i + nums[i]
            if temp > farthest:
                farthest = temp
                
            # When we hit the end of the current jump window, increment jump and expand window
            if i == current_end:
                jumps += 1
                current_end = farthest
                
                # Early exit if the current window can already reach the end
                if current_end >= n - 1:
                    break
                    
        return jumps