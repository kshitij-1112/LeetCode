class Solution:

  def lengthOfLastWord(self, s: str) -> int:
    i = len(s) - 1
    length = 0

    # Step 1: Skip trailing spaces from the right
    while i >= 0 and s[i] == ' ':
      i -= 1

    # Step 2: Count the characters of the last word
    while i >= 0 and s[i] != ' ':
      length += 1
      i -= 1

    return length