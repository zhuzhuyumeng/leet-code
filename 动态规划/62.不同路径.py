class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0 for i in range(n)] for i in range(m)]
        for i in range(m):
            dp[i][0] = 1
        for j in range(n):
            dp[0][j] = 1
        for i in range(1,m): # 高度
            for j in range(1,n): #宽度
                    dp[i][j] = dp[i-1][j]+dp[i][j-1]
        return dp[-1][-1]

# dp数组代表前面的路径和
# dp[i][j]= dp[i-1][j]+dp[i][j-1]
# 初始化一个二维数组全给零！！初始的呢
# 怎么遍历呢，一层一层遍历吗，含左边
        # direct = [(0, 1), (1, 0)]  # 右，下
        # def dfs(y,x):
        #     if y==m-1 and x==n-1:
        #         return 1
        #     res = 0
        #     if y+direct[1][0]<m:
        #         res += dfs(y+1,x)
        #     if x+direct[0][1]<n:
        #         res += dfs(y,x+1)
        #     return res
        # y = 0
        # x = 0
        # res = dfs(y,x)
        # return res

"""
0 0 0
0 0 0
0 0 0
"""
if __name__ =="__main__":
    m=3 # 宽
    n=7 # 长
    sol = Solution()
    print(sol.uniquePaths(m,n))