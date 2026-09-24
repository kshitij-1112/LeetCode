class Solution:
    def jump(self, nums: list[int]) -> int:
        jumps = 0
        current_end = 0
        farthest = 0
        
        # We iterate up to len(nums) - 1 because we don't need to jump *from* the last index
        for i in range(len(nums) - 1):
            # Track the maximum index reachable from any point in the current range
            farthest = max(farthest, i + nums[i])
            
            # If we've reached the boundary of our current jump, we must take another jump
            if i == current_end:
                jumps += 1
                current_end = farthest
                
                # Optimization: if the current jump range already reaches the end, exit early
                if current_end >= len(nums) - 1:
                    break
                    
        return jumps