class Solution:

  def combinationSum(
      self, candidates: List[int], target: int
  ) -> List[List[int]]:
    # dp[i] will store all unique combinations that sum up to i
    dp = [[] for _ in range(target + 1)]
    dp[0] = [[]]  # Base case: one way to make sum 0 (empty combination)

    for c in candidates:
      for i in range(c, target + 1):
        for prev in dp[i - c]:
          dp[i].append(prev + [c])

    return dp[target]