class Solution:
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        # Sort the candidates to easily handle duplicates and stop early
        candidates.sort()
        res = []
        
        def backtrack(start: int, target: int, path: list[int]):
            if target == 0:
                res.append(path.copy())
                return
            
            for i in range(start, len(candidates)):
                # Skip duplicates at the same tree level to avoid identical combinations
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                
                # If the current candidate exceeds the remaining target, stop the loop (since array is sorted)
                if candidates[i] > target:
                    break
                
                path.append(candidates[i])
                backtrack(i + 1, target - candidates[i], path)
                path.pop()
                
        backtrack(0, target, [])
        return res