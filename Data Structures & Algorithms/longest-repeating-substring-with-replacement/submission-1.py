class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        charSet = set(s)
        res = 0
        for c in charSet:
            
            for i in range(len(s)):
                substr = ""
                ch = i
                ktemp = k
                while ch < len(s) and (s[ch] == c or ktemp > 0):
                    
                    if s[ch] == c:
                        substr+=s[ch]
                    else:
                        substr+=c
                        ktemp-=1
                    ch+=1
                res = max(res,len(substr))
        return res
                
