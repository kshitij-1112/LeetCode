class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()  # Sort to group duplicates together
        
        def backtrack(start, current_subset):
            res.append(current_subset.copy())
            
            for i in range(start, len(nums)):
                # Skip adjacent duplicates at the same recursion level
                if i > start and nums[i] == nums[i - 1]:
                    continue
                
                current_subset.append(nums[i])
                backtrack(i + 1, current_subset)
                current_subset.pop()
                
        backtrack(0, [])
        return res