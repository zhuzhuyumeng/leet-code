import sys
from collections import defaultdict

# 你可能是对的但是超时了
class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        n = len(nums)
        if n<k:
            return
        llist = []
        sum=0
        cnt = dict()
        for i in range(n):
            cnt[i] = nums[i]
            if i>=k:
                cnt.pop(i-k)
            if i>=k-1:
                max_sum = -sys.maxsize
                for j in cnt:
                    max_sum = max(max_sum,cnt[j])
                llist.append(max_sum)
        return llist


nums = [1,3,-1,-3,5,3,6,7]
k = 3
print(Solution.maxSlidingWindow(Solution,nums,k))
# 这个滑动窗口是求每个窗口的最大值