class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        if not nums:
            return 0
        start, end = 0, 0
        n = len(nums)
        total = 0
        ans = n+1
        while end<n :
            total += nums[end]
            while total >= target: # 只有while可以减到底，再重新计算
                ans = min(ans,end-start+1)
                total -= nums[start]
                start += 1
            end += 1
        if ans == n + 1:
            return 0
        else:
            return ans
# 数字达不到的情况也要考虑
# target = 7
# nums = [2,3,1,2,4,3]
target = 11
nums = [1,1,1,1,1,1,1,1]
print(Solution.minSubArrayLen(Solution,target,nums))
