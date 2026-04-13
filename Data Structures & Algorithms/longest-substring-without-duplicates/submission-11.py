class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        l = 0
        sub = set(s[0])
        res = 1
        for i in range(1,len(s)):
            c = s[i]
            if c not in sub:
                res = max(res, i - l + 1)     
            else:
                while s[l] != c:
                    sub.remove(s[l])
                    l += 1
                l += 1
                print('New l at: ', l)
            sub.add(c)
        return res
        