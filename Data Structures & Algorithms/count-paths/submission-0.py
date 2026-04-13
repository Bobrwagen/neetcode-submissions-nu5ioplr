class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0] * n for _ in range(m)]

        # Fill the last row and last column with 1s
        for i in range(n):
            dp[m - 1][i] = 1
        for i in range(m):
            dp[i][n - 1] = 1


        for d in dp:
            print(d)  
        
        for i in range(n-2,-1,-1):
            for j in range(m-2,-1,-1):
                dp[j][i] = dp[j+1][i] + dp[j][i+1]
        
        for d in dp:
            print(d)
        return dp[0][0]


        