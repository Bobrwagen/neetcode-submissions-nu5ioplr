class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        has = {}
        for i in range(len(s1)):
            has[s1[i]] = 1 + has.get(s1[i], 0)
        
        left = 0
        right = len(s1) - 1
        while right < len(s2):
            curr = {}
            for i in range(left, right + 1):
                curr[s2[i]] = 1 + curr.get(s2[i], 0)
            if curr == has:
                return True
            else:
                left += 1
                right += 1
        return False