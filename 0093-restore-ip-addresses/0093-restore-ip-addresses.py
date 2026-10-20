class Solution:

    def restoreIpAddresses(self, s: str) -> List[str]:
        res = []
        n = len(s)

        # Quick pruning: an IPv4 address must have between 4 and 12 digits
        if n < 4 or n > 12:
            return res

        def backtrack(start: int, path: list):
            # If we have 4 segments and have consumed the whole string, it's valid
            if len(path) == 4:
                if start == n:
                    res.append(".".join(path))
                return

            # We need 4 segments total. If remaining characters are too many or too few, prune early.
            remaining_segments = 4 - len(path)
            remaining_chars = n - start
            if (
                remaining_chars < remaining_segments
                or remaining_chars > remaining_segments * 3
            ):
                return

            # Try taking 1, 2, or 3 digits for the current segment
            for end in range(start, min(start + 3, n)):
                segment = s[start : end + 1]

                # Validation checks:
                # 1. No leading zeros (e.g., "01" is invalid, but "0" is valid)
                # 2. Value must be <= 255
                if (segment[0] == "0" and len(segment) > 1) or int(
                    segment
                ) > 255:
                    continue

                # Choose -> Explore -> Unchoose (Backtrack)
                path.append(segment)
                backtrack(end + 1, path)
                path.pop()

        backtrack(0, [])
        return res