class Solution:

    def minWindow(self, s: str, t: str) -> str:
        if not s or not t or len(s) < len(t):
            return ""

        # Frequency array for ASCII characters
        target_count = [0] * 128

        # Count frequencies of characters in t
        for char in t:
            target_count[ord(char)] += 1

        required = len(t)
        left = 0
        min_len = float("inf")
        start_idx = 0

        # Expand the window using the right pointer
        for right, char in enumerate(s):
            char_ascii = ord(char)

            # If the character is needed, decrement the required count
            if target_count[char_ascii] > 0:
                required -= 1

            # Decrement frequency in our tracker array
            target_count[char_ascii] -= 1

            # When window has all required characters, try to contract it
            while required == 0:
                window_len = right - left + 1
                if window_len < min_len:
                    min_len = window_len
                    start_idx = left

                left_char_ascii = ord(s[left])
                target_count[left_char_ascii] += 1

                # If character count becomes positive, it's a required character for string t
                if target_count[left_char_ascii] > 0:
                    required += 1

                left += 1

        return (
            ""
            if min_len == float("inf")
            else s[start_idx : start_idx + min_len]
        )