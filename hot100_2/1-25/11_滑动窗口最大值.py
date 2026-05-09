import sys
from collections import deque


class Solution:
    def maxSlidingWindow(self,nums:list[int],k:int) -> list[int]:
        ans = []
        n = len(nums)
        hashtable = dict() # 用来存储数组的数字以及个数
        for i in range(n):
            hashtable[i] = nums[i]
            if i>=k: #数量超出k，弹出前面的数字
                hashtable.pop(i-k)
            if i>=k-1: #数量刚满足k
                maxnum = -sys.maxsize
                for j in hashtable: # 遍历哈希表找最大值
                    maxnum  = max(maxnum,hashtable[j])
                ans.append(maxnum)
        return ans
    def chuli(self,nums:list[int],k:int)->list[int]:
        queue = deque()
        n = len(nums)
        res = []
        for i,num in enumerate(nums):
            while queue and queue[0]<=i-k: #队列存在且队列第一个数字位置小于当前窗口头的位置
                queue.popleft()
            while queue and num>=nums[queue[-1]]:# 如何维护单调递减？新数字比最后一个数字大
                queue.pop()
            queue.append(i)
            if i>=k-1:
                res.append(nums[queue[0]])
        return res

"""
用什么动态保存最大值？
"""
if __name__ == "__main__":
    nums = [1,3,-1,-3,5,3,6,7]
    k = 3
    print(Solution.chuli(Solution,nums,k))