class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1
        res = 0
        while l <= r:
            if heights[l] <= heights[r]:
                res = max(res, (r-l) * min(heights[l], heights[r]))
                l += 1
            else:
                res = max(res, (r-l) * min(heights[l], heights[r]))
                r -= 1
            print(res,l,r)
        return res