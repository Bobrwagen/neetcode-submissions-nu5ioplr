class Solution:
    def isHappy(self, n: int) -> bool:
        vis = set()
        while n != 1:
            tmp = str(n)
            cur = 0
            for c in tmp:
                cur += int(c) ** 2
            if cur in vis:
                return False
            else:
                 vis.add(cur)
                 n = cur
        return True
        