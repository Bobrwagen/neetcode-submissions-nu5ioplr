class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = {'' : True}
        for i in range(len(s)):
            sub = s[0:i+1]
            dp[sub] = False
            for w in wordDict:
                if sub.endswith(w):
                    dp[sub] = dp[sub.removesuffix(w)] or dp[sub]
        return dp[s]
