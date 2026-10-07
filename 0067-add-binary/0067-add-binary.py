class Solution:

  def addBinary(self, a: str, b: str, i=0, j=0, carry=0) -> str:
    # Using built-in int conversion with base 2 is implemented in C under the hood,
    # making it exceptionally fast on LeetCode's backend.
    return bin(int(a, 2) + int(b, 2))[2:]