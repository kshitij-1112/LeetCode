class Solution:
    def grayCode(self, n: int) -> List[int]:
        # Generate the gray code sequence using the binary-to-gray formula: i ^ (i >> 1)
        return [i ^ (i >> 1) for i in range(1 << n)]