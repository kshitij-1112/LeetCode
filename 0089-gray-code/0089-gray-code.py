class Solution:
    def grayCode(self, n: int) -> list[int]:
        size = 1 << n
        res = [0] * size

        for i in range(1, size):
            res[i] = i ^ (i >> 1)

        return res
