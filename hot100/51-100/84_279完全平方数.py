import math
import sys


class Solution:
    def numSquares(self, n: int) -> int:
        sqrt_num = int(math.sqrt(n))
        print(sqrt_num)
        dp = [sys.maxsize]*(n+1)
        dp[0] = 0
        for i in range(n+1):
            for j in range(1,sqrt_num+1):
                if j*j<=i:
                    dp[i] = min(dp[i],dp[i-j*j]+1)
                else:
                    dp[i] = dp[i]
        return dp[n]
"""
这题是要找最小的数字
1.dp数组以及下标含义：横轴是数字的个数，纵轴是最大的数字当前数字最大的和
dp[j]容量为j的背包装的最小数字组成
2.推导式：dp[]
dp[i] = 
3.dp数组初始化
4.确定遍历顺序
5.举例推导
"""

if __name__ == "__main__":
    n = 12
    sol = Solution()
    print(sol.numSquares(n))