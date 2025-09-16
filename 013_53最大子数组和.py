import sys
from collections import defaultdict


class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        cnt = defaultdict(int)
        cnt[0] = 1
        sum = 0
        minsum = 0
        maxsum = -sys.maxsize
        for index,value in enumerate(nums):
            sum += value
            cnt[sum] +=1
            if maxsum < sum:
                maxsum = sum
            if minsum > sum:
                minsum = sum
        result = maxsum-minsum
        return result



# nums = [-2,1,-3,4,-1,2,1,-5,4]
nums = [1]
print(Solution.maxSubArray(Solution,nums))
# 前缀和？