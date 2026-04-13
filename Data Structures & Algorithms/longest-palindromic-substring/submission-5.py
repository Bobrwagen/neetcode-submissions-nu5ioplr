class Solution:
    def longestPalindrome(self, s: str) -> str:
        left = 0
        right = len(s) - 1
        res = s[0]
        def is_Pal(st):
            l = 0
            r = len(st) - 1
            while l <= r:
                if st[l] != st[r]:
                    return False
                l += 1
                r -= 1
            return True

        while left <= right:
            left_ind = left
            right_ind = right
            while left_ind < right_ind:
                sub = s[left_ind:right_ind+1]
                if is_Pal(sub):
                    if len(sub) > len(res):
                        res = sub
                right_ind -= 1
            left_ind = left
            right_ind = right
            while left_ind < right_ind:
                sub = s[left_ind:right_ind+1]
                if is_Pal(sub):
                    if len(sub) > len(res):
                        res = sub
                left_ind += 1
            left += 1
            right -= 1
        return res    

            

        