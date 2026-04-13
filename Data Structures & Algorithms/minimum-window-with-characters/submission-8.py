class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # remaining words
        count = defaultdict(int)
        window = defaultdict(int)
        have = 0
        resStr = [-1,-1]
        resLen = float('infinity')
        for c in t:
            count[c] += 1
        need = len(count)
        l = 0
        for r in range(len(s)):
            print((l,r))
            c = s[r]
            window[c] += 1
            if c in count and window[c] == count[c]:
                have +=1
            
            while have == need:
                newLen = r - l +1
                if newLen < resLen:
                    resLen = newLen
                    resStr = [l, r+1]
                window[s[l]] -= 1
                if s[l] in count and window[s[l]] < count[s[l]]:
                    have -=1
                l += 1
        l,r = resStr
        return s[l:r] if resLen != float('infinity') else ''


                