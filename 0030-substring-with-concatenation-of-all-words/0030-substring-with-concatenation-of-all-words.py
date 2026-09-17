from collections import Counter


class Solution:

  def findSubstring(self, s: str, words: list[str]) -> list[int]:
    if not s or not words:
      return []

    word_len = len(words[0])
    num_words = len(words)
    window_len = word_len * num_words
    s_len = len(s)

    if s_len < window_len:
      return []

    word_count = Counter(words)
    result = []

    # Slide window across each possible word offset alignment
    for i in range(word_len):
      left = i
      current_count = Counter()
      valid_count = 0

      for right in range(i, s_len - word_len + 1, word_len):
        word = s[right : right + word_len]

        if word in word_count:
          current_count[word] += 1
          valid_count += 1

          # Shrink window from the left if a word count exceeds target frequency
          while current_count[word] > word_count[word]:
            left_word = s[left : left + word_len]
            current_count[left_word] -= 1
            valid_count -= 1
            left += word_len

          # Record the starting index when all target words match the window
          if valid_count == num_words:
            result.append(left)
        else:
          # Reset the window immediately upon encountering an invalid word
          current_count.clear()
          valid_count = 0
          left = right + word_len

    return result