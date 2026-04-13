class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        left = 0
        right = 0
        seq = {}
        while right < len(s):
            l = 0
            while s[right] not in seq.keys():
                l = right - left + 1
                res = max(res,l)
                seq[s[right]] = right
                right += 1
                if right == len(s):
                    break
            if right == len(s):
                break
            temp = seq[s[right]] + 1
            while left < temp:
                seq.pop(s[left])
                left += 1

        return res
        