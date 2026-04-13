class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        res = r
        while l <= r:
            mid = (l + r) // 2
            cur = 0
            for p in piles:
                cur += math.ceil(float(p) / mid)
            if cur <= h:
                res = mid
                r = mid - 1
            else:
                l = mid + 1
        return res