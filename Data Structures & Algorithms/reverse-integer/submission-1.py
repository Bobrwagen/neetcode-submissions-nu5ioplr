class Solution:
    def reverse(self, x: int) -> int:
        sign = x
        abso = abs(x)
        s = str(abso)[::-1]
        s = int(s)
        if sign < 0:
            s *= -1
        if s < -(1 << 31) or s > (1 << 31) - 1:
            return 0
        return s