import sys


class Solution:
    def maxSubArraydp(self,nums:list[int]) -> int:
        n = len(nums)
        dp = [0]*n
        dp[0] = nums[0]

        for i in range(1,n):
            if dp[i-1]<0:
                # 前面数组的和小于0，直接不鸟
                dp[i] = nums[i]
            else:
                dp[i] = dp[i-1]+nums[i]
        return max(dp)

    def maxSubArray(self,nums:list[int]) -> int:
        # 一个前缀和统计，一个最大值统计，一个最小值统计初始化为0,第一个数字不需要，（时间顺序在最大值之前）
        ans = -sys.maxsize
        sum = 0
        minsum = 0
        for i in range(len(nums)):
            sum += nums[i]
            ans = max(ans,sum-minsum)
            minsum = min(sum,minsum)
        return ans

    def maxSubArray2(self,nums:list[int]) -> int:
        sum = 0
        ans = -sys.maxsize
        minsum = 0#还没看任何元素之前，最小前缀和是0
        for i in range(len(nums)):
            sum += nums[i] # 当前前缀
            minsum = min(minsum,sum) # 最小前缀=之前最小vs当前
            ans = max(ans,sum-minsum) # 最大前缀和=之前最大vs当前最小
        return ans
"""
使用最大最小值不好处理啊，最大值需要在最小值的前面，只可以用当前的值减去前面的最小值
"""
if __name__ == "__main__":
    # nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    nums = [1]
    print(Solution.maxSubArray2(Solution,nums))