class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        position = 32
        for i in range(position):
            bit = (n >> i) & 1
            res |= (bit << (position - i - 1))
        return res