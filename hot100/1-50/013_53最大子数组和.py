import sys
from collections import defaultdict


class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        ans = -sys.maxsize # 存放最大值
        sum = 0
        minsum = 0
        for index,value in enumerate(nums):
            sum += value # 统计每个数字的所有前缀
            ans = max(ans,sum-minsum) # 当前前缀和及最小值
            minsum = min(sum,minsum) # 找到最小值
        return ans



# nums = [-2,1,-3,4,-1,2,1,-5,4]
# nums = [1]
# nums = [-1]
nums = [-2,1]
print(Solution.maxSubArray(Solution,nums))
# 前缀和？，第一个0我不会处理