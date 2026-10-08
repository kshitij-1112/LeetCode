class Solution:
    def fullJustify(self, words: list[str], maxWidth: int) -> list[str]:
        res = []
        i = 0
        n = len(words)

        while i < n:
            # Find the maximum number of words that fit on this line.
            j = i
            line_len = 0

            while j < n and line_len + len(words[j]) + (j - i) <= maxWidth:
                line_len += len(words[j])
                j += 1

            count = j - i
            spaces = maxWidth - line_len

            # Last line OR line with only one word -> left justified.
            if j == n or count == 1:
                line = " ".join(words[i:j])
                res.append(line + " " * (maxWidth - len(line)))

            else:
                gaps = count - 1
                even_space = spaces // gaps
                extra = spaces % gaps

                # Left gaps get one additional space each.
                parts = []
                for k in range(gaps):
                    parts.append(words[i + k])
                    parts.append(" " * (even_space + (k < extra)))

                parts.append(words[j - 1])
                res.append("".join(parts))

            i = j

        return res