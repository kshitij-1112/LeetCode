class Solution:

  def isNumber(self, s: str) -> bool:
    seen_digit = False
    seen_exponent = False
    seen_dot = False

    for i, char in enumerate(s):
      if char.isdigit():
        seen_digit = True
      elif char in "+-":
        # A sign is only valid at the very beginning or immediately following 'e' or 'E'
        if i > 0 and s[i - 1] != "e" and s[i - 1] != "E":
          return False
      elif char == ".":
        # A dot cannot appear if we already saw a dot or an exponent (since exponents must be integers)
        if seen_dot or seen_exponent:
          return False
        seen_dot = True
      elif char in "eE":
        # An exponent cannot appear if we already saw one, or if we haven't seen any digit yet
        if seen_exponent or not seen_digit:
          return False
        seen_exponent = True
        seen_digit = False  # Reset because an exponent must be followed by digits
      else:
        return False

    # The string must end with a valid digit (e.g., "e" or "." alone are invalid)
    return seen_digit