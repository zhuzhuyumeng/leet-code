from typing import List
class Solution:
    def lastStoneWeightII(self,stones:List[int])->int:
        count = sum(stones)
        target = count//2
        dp = [0]*(target+1)

        for j,stone in enumerate(stones):
            for i in range(target,-1,-1):
                if stone>i:
                    dp[i] = dp[i]
                else:
                    dp[i] = max(dp[i],dp[i-stone]+stone)

        res = (count - dp[target])-dp[target] #另一组减去这一组
        return res

"""
这题和01背包都是一个只能用一次，这是要最小。原来是分成两个重量相近的组合吗，但是这是不确定的呀

1.dp数组以及下标的含义
dp[j]表示容量为j的背包，所能装载的最大价值dp[j]
注意这是最大的价值
2.递推方程
dp[i] = max(dp[i],dp[i-stone]+stone)
3.dp数组初始化

4.确定遍历顺序

5.举例

"""


if __name__ == '__main__':
    stones = [2,7,4,1,8,1]
    print(Solution.lastStoneWeightII(Solution,stones))