import sys
from collections import defaultdict, deque


# 你可能是对的但是超时了
class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        ans = [0]*(len(nums)-k+1)
        q = deque() # 只表示位置
        for i,x in enumerate(nums): # 单调减
            while q and nums[q[-1]]<=x:
                q.pop()
            q.append(i) # 更新完毕

            left = i-k+1 # 窗口左
            if q[0]<left: # 远离窗口
                q.popleft()

            if left>=0:
                ans[left] = nums[q[0]]
        return ans
    womeizhao


# 第一步维护好这个单调队列
# 第二步排除本该离开窗口的数字
# 第三步写答案






        # n = len(nums)
        # q = deque()
        # ans = [0]*(n-k+1) # 为什么窗口个数是这个，而不是k。这是用来存放答案的
        # for i,x in enumerate(nums):
        #     while q and nums[q[-1]] <= x:# 队列最后一个数字比当前的小
        #         q.pop()
        #     q.append(i)
        #
        #     left = i-k+1 # 当前窗口左的位置，如果当前数字远离了窗口，最大弹出
        #     if q[0]<left:
        #         q.popleft()
        #
        #     if left>=0:
        #         ans[left] = nums[q[0]]
        # return ans



nums = [1,3,-1,-3,5,3,6,7]
k = 3
print(Solution.maxSlidingWindow(Solution,nums,k))
# 这个滑动窗口是求每个窗口的最大值