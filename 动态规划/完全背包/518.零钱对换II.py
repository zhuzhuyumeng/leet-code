import sys
from typing import List
class Solution:
    def change(self,amount: int,coins: List[int]) ->int:
        dp = [0]*(amount+1)
        dp[0] = 1
        for j, coin in enumerate(coins):
            for i in range(coin, amount + 1): #
                # 一轮遍历就是当前数字和之前数字的硬币组合数
                dp[i] += dp[i-coin]
        return dp[amount]


    def change2(self, amount: int, coins: List[int]) -> int:
        coin_num = len(coins)
        dp = [[0]*(amount+1) for _ in range (coin_num)]
        dp[0][0] = 1
        for i in range(coins[0],amount+1):
            dp[0][i] = dp[0][i-coins[0]]

        for j in range(1,coin_num):
            coin = coins[j]
            for i in range(amount+1):
                if coin<=i:
                    dp[j][i] = dp[j-1][i] + dp[j][i-coin] #本来的结果加上新硬币加入的结果
                else:
                    dp[j][i] = dp[j - 1][i]

        return dp[coin_num-1][amount]
        # ans = 0
        # dp = [sys.maxsize]*(amount+1)
        # dp[0] = 0
        # for j, coin in enumerate(coins):
        #     for i in range(1,amount+1):
        #         if coin<=i:
        #             if dp[i]>dp[i-coin]:
        #                 dp[i] = dp[i-coin]+1
        #                 if i==amount:
        #                     ans+=1
        #         else:
        #             dp[i] = dp[i]
        # return ans
"""
是不是有点像跳台阶
1.dp数组以及下标含义
dp[j]表示价值j的组成硬币的组合数
2.递推公式

3.dp数组初始化
dp[0]初始化为1因为直接可达，其他设置为0
4.遍历顺序
价值从小到大正序遍历
先重量后硬币导致变成了组成的数量
5.举例推导
i 0 1 2 3 4 5
  1 0 0 0 0 0
  1 1 1 1 1 1
  1 1 2 2 3 3
  1 1 2 2 3 4
"""
if __name__ == "__main__":
    amount = 5
    coins = [1, 2, 5]
    print(Solution.change(Solution,amount,coins))
