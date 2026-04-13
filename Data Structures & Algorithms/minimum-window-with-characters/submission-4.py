class Solution:
    def minWindow(self, s: str, t: str) -> str:
        chars_left = {}
        for c in t:
            chars_left[c] = 1 + chars_left.get(c,0)
        vis = {}
        res = ""
        reslen = float("infinity")
        for r in range(len(s)):
            if s[r] in t:
                if s[r] not in chars_left:
                    vis[s[r]].pop(0)
                    vis[s[r]].append(r)
                else:
                    if chars_left[s[r]] - 1 == 0:
                        chars_left.pop(s[r])
                        if s[r] not in vis:
                            vis[s[r]] = []
                        vis[s[r]].append(r)
                    else:
                        chars_left[s[r]] -= 1
                        if s[r] not in vis:
                            vis[s[r]] = []
                        vis[s[r]].append(r)
            if chars_left == {}:
                vals = []
                for v in vis.values():
                    vals += v
                if max(vals) - min(vals) < reslen:
                    res = s[min(vals): max(vals) + 1]
                    reslen = max(vals) - min(vals)
        return res