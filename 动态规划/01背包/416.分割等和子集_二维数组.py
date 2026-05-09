from typing import List
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n = len(nums) #数组个数
        if n<=1:
            return False
        total = sum(nums)
        print(total & 1)
        if total & 1:
            return False
        target = int(total/2)

        dp = [[0]*(target+1) for i in range(n)]

        for i,num in enumerate(nums): #数组个数
            dp[i][0] = 1

        # for i, num in enumerate(nums):
        #     for j in range(target+1):
        #         dp[i][j] = dp[i - 1][j]
        #         if j-num>0:
        #             dp[i][j] = dp[i - 1][j] or dp[i - 1][j - num]
        #         # 上一排的该数字的值或者上一排的该数减去num的值 10 = 0 + 9
        #         if num<=j: #当前数字小于范围，这把所有数字变成了符合
        #             dp[i][num] = 1

        dp[0][nums[0]] = 1

        for i in range(1,n):
            for j in range(1,target+1):
                dp[i][j] = dp[i-1][j]#常规保底情况
                if nums[i]<=j:
                    dp[i][j] = dp[i-1][j-nums[i]]


        for i in range(n):
            print(dp[i])
        if dp[n-1][target]==1:
            return True
        else:
            return False

"""
五部曲
1.dp数组以及下标的含义：
dp[n][n]横坐标表示目标重量能否被组合出来
纵坐标表示已有的数组

2.递推方程：
for i,num in enumerate(nums):
    for j in range(target):
        dp[i][j] = dp[]
        if j > num:
        dp[i][j] = dp[i][j-num]
        
根据上一排的结果，在当前值为Ture的横坐标+当前数字的横坐标改为True
如果目标重量的变成True就可以返回True了

3.dp数组初始化：第一行就是每个数组的数字都放进去
纵坐标第一排，重量为0是True，后面均为False。
4.确定遍历顺序：
5.举例推导：
10
   0  1  2  3
0  1  5  9  5
1  1  6  10 10
2
3
这是不对的
"""

if __name__ == "__main__":
    # nums = [1,5,9,5]
    nums = []
    print(Solution.canPartition(Solution,nums))