from typing import List
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total%2 : #不能完整被2取模，不是2的倍数
            return False
        n = total//2
        dp = [False]*(n+1)
        dp[0] = True

        for j, num in enumerate(nums):
            for i in range(n,-1,-1):
                if nums[j]<=i:
                    dp[i] = dp[i]|dp[i-nums[j]]
        print(dp)
        return dp[n]

"""
这是有限个数
先物品，后重量，而且是后序遍历

"""
if __name__ == "__main__":
    nums = [1, 5, 11, 5]
    print(Solution.canPartition(Solution,nums))