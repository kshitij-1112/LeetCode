class Solution:

  def merge(self, intervals: list[list[int]]) -> list[list[int]]:
    # Sort the intervals based on the start time
    intervals.sort(key=lambda x: x[0])

    merged = []
    for interval in intervals:
      # If the merged list is empty or there is no overlap, append the interval
      if not merged or merged[-1][1] < interval[0]:
        merged.append(interval)
      else:
        # There is an overlap, so merge by updating the end time
        merged[-1][1] = max(merged[-1][1], interval[1])

    return merged