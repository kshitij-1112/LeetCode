from itertools import groupby


class Solution:

  def countAndSay(self, n: int) -> str:
    current = "1"

    for _ in range(n - 1):
      # C-optimized run-length encoding via groupby
      current = "".join(
          f"{len(list(group))}{key}" for key, group in groupby(current)
      )

    return current