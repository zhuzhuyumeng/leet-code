from typing import List
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        nums_length = len(nums)
        dp = [1]*(nums_length)
        for i in range(nums_length):
            for j in range(i):
                if nums[i]>nums[j]:
                    dp[i] = max(dp[i],dp[j]+1)
        res = 0
        for i in range(nums_length):
            res = max(res, dp[i])
        print(dp)
        return res
"""
1.dp数组以及下标的含义
dp[j]表示位置j的数组元素可以构成的最长严格递增子序列
2.递推公式
如何进行递推，数组的更新
if num[i]>nums[j]:
    dp[i] = max(dp[i],dp[j]+1)
3.dp数组初始化
初始化为全1，因为没有递增数组的话，数字本身也是1
4.遍历顺序
根据数组长度，再对之前的数组
5.举例推导
  10 9 2 5 3 7 101 18
0 1  2 3 4 5 6 7   8
0 1  1 1 2 2 3 4   4
1 
"""

if __name__ == "__main__":
    nums = [10,9,2,5,3,7,101,18]
    print(Solution.lengthOfLIS(Solution,nums))