import sys
from typing import List
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [sys.maxsize]*(amount+1)
        dp[0] = 0
        for j,coin in enumerate(coins):
            for i in range(coin,amount+1):
                dp[i] = min(dp[i],dp[i-coin]+1)

        if dp[amount]==sys.maxsize:
            return -1
        else:
            return dp[amount]

"""
1.dp数组以及下标的含义
dp[j]表示要达到j的价值，当前的最少重量，一个硬币一重量
2.递推公式
dp[i] = min(dp[i],dp[i-coin]+1)
在当前的最小重量和新硬币的最小重量进行对比
3.dp数组初始化
dp[0]=0其他全为最大值，因为我们要取最小值
4.遍历顺序
从每个硬币，正序扫一遍价值，可以做到无限多个硬币
5.举例推导

"""


if __name__ == "__main__":
    coins = [1, 2, 5]
    amount = 11
    print(Solution.coinChange(Solution,coins,amount))