from typing import List
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        for i in range(1,n):
            grid[0][i] = grid[0][i-1]+ grid[0][i]
        for i in range(1,m):
            for j in range(n):
                if j==0:
                    grid[i][j] = grid[i][j] + grid[i - 1][j]
                else:
                    grid[i][j] = min(grid[i][j]+grid[i-1][j],grid[i][j]+grid[i][j-1])
        print(grid)
        return grid[m - 1][n - 1]
        # dp = [[0 for i in range(n)]for i in range(m)]
        # for i in range(n):
        #     dp[0][i] = dp[0][i-1]+ grid[0][i]
        # for i in range(1,m):
        #     for j in range(n):
        #         if j==0:
        #             dp[i][j] = grid[i][j] + dp[i - 1][j]
        #         else:
        #             dp[i][j] = min(grid[i][j]+dp[i-1][j],grid[i][j]+dp[i][j-1])
        #             # 有数字本身和处理后的dp数组
        # return dp[m-1][n-1]

"""
1.dp数组以及下标的含义
dp[i][j]对应位置的最短数字和
2.状态转移方程
dp[i][j] = min(grid[i][j]+dp[i-1][j],grid[i][j]+dp[i][j-1])
5.举例推导
0 1 2
1 4 5
2 7 

"""

if __name__ == "__main__":
    grid = [[1,3,1],[1,5,1],[4,2,1]]
    grid = [[1, 2, 3], [4, 5, 6]]
    print(Solution.minPathSum(Solution,grid))