class Solution:
    def countBits(self, n: int) -> List[int]:
        res = []
        for i in range(n+1):
            if i < 2:
                res.append(i & 1)
            else:
                print(i)
                val = res[i//2] + (i & 1)
                res.append(val)
        return res