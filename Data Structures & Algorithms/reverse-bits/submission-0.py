class Solution:
    def reverseBits(self, n: int) -> int:
        rev = 0
        for i in range(31,-1,-1):
            rev += (n & 1) << i
            n = n >> 1
        return rev

            
        