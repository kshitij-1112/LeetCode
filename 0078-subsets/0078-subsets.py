class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        for num in nums:
            # Append the current number to all existing subsets and add them
            res.extend([curr + [num] for curr in res])
        return res