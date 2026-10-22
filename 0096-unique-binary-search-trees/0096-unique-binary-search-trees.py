class Solution:

  def numTrees(self, n: int) -> int:
    # Using the Catalan number iterative formula: C_n = (2(2n-1) / (n+1)) * C_{n-1}
    catalan = 1
    for i in range(1, n + 1):
      catalan = catalan * 2 * (2 * i - 1) // (i + 1)
    return catalan