class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        l = 0
        vis = set()
        res = 0
        for r in range(len(s)):
            while s[r] in vis:
                    vis.remove(s[l])
                    l += 1
            vis.add(s[r])
            res = max(r-l+1, res)
        return res

        