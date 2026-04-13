class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0
        for i in range(len(s)):
            # odd
            left,right = i,i
            while left > -1 and right < len(s) and s[left] == s[right]:
                res += 1
                left -= 1
                right += 1
            
            # even
            left,right = i, i+1
            while left > -1 and right < len(s) and s[left] == s[right]:
                res += 1
                left -= 1
                right += 1
        return res
        