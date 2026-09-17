class Solution:

  def findSubstring(self, s: str, words: list[str]) -> list[int]:
    if not s or not words:
      return []

    word_len = len(words[0])
    num_words = len(words)
    total_len = word_len * num_words
    s_len = len(s)

    if s_len < total_len:
      return []

    # Build frequency map using a primitive dictionary
    word_count = {}
    for w in words:
      word_count[w] = word_count.get(w, 0) + 1

    result = []
    
    # Iterate through each word-length offset
    for i in range(word_len):
      left = i
      right = i
      current_count = {}
      valid_words = 0

      while right + word_len <= s_len:
        word = s[right : right + word_len]
        right += word_len

        if word in word_count:
          current_count[word] = current_count.get(word, 0) + 1
          valid_words += 1

          # Shrink window if count exceeds target frequency
          while current_count[word] > word_count[word]:
            left_word = s[left : left + word_len]
            current_count[left_word] -= 1
            valid_words -= 1
            left += word_len

          if valid_words == num_words:
            result.append(left)
        else:
          current_count.clear()
          valid_words = 0
          left = right

    return result