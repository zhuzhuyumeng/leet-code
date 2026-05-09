from typing import List
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = [0]*(len(cost)+1)
        for i in range(2,len(cost)+1):
            dp[i] = min(dp[i-1]+cost[i-1],dp[i-2]+cost[i-2])
        return dp[-1]

# dp数组含义，前面两个或一个的最小值+本身
# dp推导公式
# dp数组初始化
# 确定遍历顺序
# 举例推导DP
if __name__ == "__main__":
    cost = [10,15,20]
    sol = Solution()
    print(sol.minCostClimbingStairs(cost))