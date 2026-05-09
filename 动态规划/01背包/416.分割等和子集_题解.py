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

        dp = [0]*(target+1)

        for j, num in enumerate(nums):
            for i in range(target,-1,-1):
                if i>=num:
                    dp[i] = max(dp[i],dp[i-num]+num)
                dp[i] = dp[i]
                if dp[target] ==target:
                    return True
        return False



"""
五部曲
1.dp数组以及下标的含义：
dp[j]表示容量为j的背包，所能背的最大物品价值为dp[j]，本题当dp[target]=target时符合条件
2.递推方程：

dp[j] = max(dp[j],dp[j - num[i]] + nums[i])

3.dp数组初始化：第一行就是每个数组的数字都放进去
dp[0]，如果题目中价值有负数，非0下标初始化为负无穷？在递推过程取得最大值
4.确定遍历顺序：
一维：物品遍历在外，背包遍历在内且倒序

5.举例推导：

"""

if __name__ == "__main__":
    # nums = [1,5,9,5]
    nums = [1,2,3]
    print(Solution.canPartition(Solution,nums))