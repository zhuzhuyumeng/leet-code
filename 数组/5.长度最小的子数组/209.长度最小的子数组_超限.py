import sys
from typing import List

class Solution:
    # def minSubArrayLen(self, target: int, nums: list[int]) -> int:
    #     nums_length = len(nums)
    #     min = sys.maxsize
    #     for i in range(nums_length):
    #         ans = 0
    #         for j in range(i,nums_length):
    #             ans += nums[j]
    #             if ans >= target and min >= (j-i+1):
    #                 min = (j-i+1)
    #                 break
    #     if min == sys.maxsize:
    #         return 0
    #     else:
    #         return min
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        right = 0
        sum = 0
        minsize = sys.maxsize
        n = len(nums)
        for right in range(n):
            sum += nums[right]
            while sum >= target:
                minsize = min(minsize, right - left + 1)
                sum-=nums[left]
                left+=1
        if minsize ==sys.maxsize:
            return 0
        return minsize
# 数字达不到的情况也要考虑
# target = 7
# nums = [2,3,1,2,4,3]
target = 4
nums = [1,4,4]
# target = 11
# nums = [1,1,1,1,1,1,1,1]
# target = 11
# nums = [1,2,3,4,5]
print(Solution.minSubArrayLen(Solution,target,nums))
