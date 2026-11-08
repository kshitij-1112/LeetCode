from typing import List


class Solution:

  def maxProfit(self, prices: List[int]) -> int:
    if not prices:
      return 0

    # Initialize states
    hold1 = -prices[0]
    release1 = 0
    hold2 = -prices[0]
    release2 = 0

    for price in prices[1:]:
      hold1 = max(hold1, -price)
      release1 = max(release1, hold1 + price)
      hold2 = max(hold2, release1 - price)
      release2 = max(release2, hold2 + price)

    return release2