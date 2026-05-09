from typing import List
class Solution:
    def numTrees(self, n: int) -> int:
        dp = [0]*(n+1)
        dp[0] = 1
        dp[1] = 1
        for i in range(2,n+1):
            for j in range(0,i):
                dp[i] = dp[i] + dp[j]*dp[i-1-j]
            # for j in range(1,i+1):
            #     dp[i] = dp[i] + dp[j-1]*dp[i-(j-1)]
        return dp[n]

# 二叉搜索树，左小右大
# 留一个作为根节点，两边进行计算个数
# 在2的时候就是一个空一个1了
# 这里只对形状做了统计
# DP数组含义
# DP推导式
# DP初始化
# DP如何遍历
# 举例DP
if __name__ =="__main__":
    n = 1
    sol = Solution()
    print(sol.numTrees(n))