class Solution:

  def insert(
      self, intervals: list[list[int]], newInterval: list[int]
  ) -> list[list[int]]:
    left, right = [], []
    s, e = newInterval

    for interval in intervals:
      if interval[1] < s:
        left.append(interval)
      elif interval[0] > e:
        right.append(interval)
      else:
        s = min(s, interval[0])
        e = max(e, interval[1])

    return left + [[s, e]] + right