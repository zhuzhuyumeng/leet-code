import sys


class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        nums_length = len(nums)
        min = sys.maxsize
        for i in range(nums_length):
            ans = 0
            for j in range(i,nums_length):
                ans += nums[j]
                if ans >= target and min >= (j-i+1):
                    min = (j-i+1)
                    break
        if min == sys.maxsize:
            return 0
        else:
            return min

# 数字达不到的情况也要考虑
# target = 7
# nums = [2,3,1,2,4,3]
target = 11
nums = [1,1,1,1,1,1,1,1]
print(Solution.minSubArrayLen(Solution,target,nums))
