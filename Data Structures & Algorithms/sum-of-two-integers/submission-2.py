class Solution:
    def getSum(self, a: int, b: int) -> int:
        carry = 0
        """
            a = 4 = 0100
            b = 7 = 0111
            res = 11 = 1011
            max signed = (1 << (n-1)) -1
            min signed = - (1 << (n-1))
            from unsigned to signed = substract (1 << n) when value >= (1 << (n-1)) 
        """
        position = 32
        res = 0
        mask = (1 << 32) - 1 # all ones 0xFFFF_FFFF

        for i in range(position):
            a_bit = (a >> i) & 1
            b_bit = (b >> i) & 1
            cur_bit = a_bit ^ b_bit ^ carry
            carry = (a_bit + b_bit + carry) >= 2
            if cur_bit:
                res |= (1 << i)
        
        if res >= (1 << (position - 1)):
            res -= (1 << position)
        return res
                         