class Solution:
    def myPow(self, x: float, n: int) -> float:
        res = 1
        for i in range(n):
            res *= x
        while n < 0:
            res /= x
            n += 1
        return res
        