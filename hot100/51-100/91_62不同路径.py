class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0 for i in range(m)] for i in range(n)]
        for i in range(m):
            dp[0][i] = 1
        for j in range(1,n):
            for i in range(m):
                dp[j][i] = dp[j-1][i]+dp[j][i-1]
                # 此处数组最后已归零所以[-1]位置不影响
        return dp[n-1][m-1]

if __name__ == "__main__":
    m = 7
    n = 3
    print(Solution.uniquePaths(Solution,m,n))