from typing import List
class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)==1:
          return nums[0]
        if len(nums)==2:
          return max(nums[0],nums[1])

        n=len(nums)
        dp=[0]*len(nums)
        dp[0]=nums[0]
        dp[1]=max(nums[0],nums[1])
        for i in range(2,n):
          dp[i]=max(dp[i-1],dp[i-2]+nums[i])
        return dp[n-1]

# dp数组表示当前屋子的最大价值
# 推导式，每个都是 前两个+现值与前一个值的比较
# 如何表示当前偷还是没有偷

if __name__ == "__main__":
    home = [1,3,1]
    sol = Solution()
    print(sol.rob(home))