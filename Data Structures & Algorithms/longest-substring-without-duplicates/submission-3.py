class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        res = ""
        length = 0
        for c in s:
            length = max(length, len(res))
            if c in res:
                res = res.split(c)[-1] + c
            else:
                res+=c
            print(res)
        return  max(length, len(res))
        