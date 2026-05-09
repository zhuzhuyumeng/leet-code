from typing import List
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        total = sum(nums)
        if total & 1: # 这是二进制吗
            return False
        target = int(total/2)
        dp = [False]*(target+1)
        dp[0] = True

        for j,num in enumerate(nums):
            for i in range(target,-1,-1): #倒序防止修改数组
                if num>i:# 当前数字放不下去
                    dp[i]=dp[i]
                else:# 这个数字或者前面的数字，取可达的
                    dp[i]=dp[i-num]|dp[i]

        return dp[target]


"""
五部曲
1.dp数组以及下标的含义：
横坐标标记权重，目标权重是和的一半
2.递推方程：
倒序遍历，取可达的
3.dp数组初始化：第一行就是每个数组的数字都放进去
整个dp为False
4.确定遍历顺序：
数组正常遍历
5.举例推导：

"""

if __name__ == "__main__":
    nums = [2,2,1,1]
    # nums = []
    print(Solution.canPartition(Solution,nums))