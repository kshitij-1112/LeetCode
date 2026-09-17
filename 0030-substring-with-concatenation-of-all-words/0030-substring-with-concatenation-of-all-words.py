from collections import Counter


class Solution:

  def findSubstring(self, s: str, words: list[str]) -> list[str]:
    if not s or not words:
      return []

    word_len = len(words[0])
    num_words = len(words)
    total_len = word_len * num_words
    s_len = len(s)

    if s_len < total_len:
      return []

    word_count = Counter(words)
    result = []

    # Iterate through each possible starting offset within the word length
    for i in range(word_len):
      left = i
      right = i
      current_count = Counter()
      valid_words = 0

      while right + word_len <= s_len:
        # Extract the next word from the right
        word = s[right : right + word_len]
        right += word_len

        if word in word_count:
          current_count[word] += 1
          valid_words += 1

          # If we have too many instances of this word, shrink from the left
          while current_count[word] > word_count[word]:
            left_word = s[left : left + word_len]
            current_count[left_word] -= 1
            valid_words -= 1
            left += word_len

          # If the valid word count matches the total words, we found a valid index
          if valid_words == num_words:
            result.append(left)
        else:
          # Reset the window if the word is not in `words`
          current_count.clear()
          valid_words = 0
          left = right

    return result