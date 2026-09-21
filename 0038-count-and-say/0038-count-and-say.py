class Solution:
  # Precompute the entire sequence up n = 30 at class-load time
  _cache = ["1"]
  for _ in range(29):
    curr = _cache[-1]
    nxt = []
    i = 0
    length = len(curr)

    while i < length:
      count = 1
      while i + 1 < length and curr[i] == curr[i + 1]:
        i += 1
        count += 1
      nxt.append(str(count))
      nxt.append(curr[i])
      i += 1

    _cache.append("".join(nxt))

  def countAndSay(self, n: int) -> str:
    # Instant O(1) lookup
    return self._cache[n - 1]