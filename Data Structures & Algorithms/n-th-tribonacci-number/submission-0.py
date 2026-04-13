class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1 or n == 2:
            return 1
        first = 1
        second = 1
        third = 0
        while n > 2:
            tmp = second
            second = first
            first += tmp + third
            third = tmp
            n -= 1
        return first
            
        