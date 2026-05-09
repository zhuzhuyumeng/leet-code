from typing import List
class Solution:
    def sortedSquares(self, nums: List[int])-> List[int]:
        n = len(nums)
        ans = []
        negative = -1
        for i,num in enumerate(nums):
            if num<0:
                negative = i
            else:
                break
        #找到正负数的交界处，即最后一个负数
        i, j = negative, negative+1
        while i>=0 or j<n:
            if i<0:
                ans.append(nums[j]*nums[j])
                j+=1
            elif j==n:
                ans.append(nums[i] * nums[i])
                i -= 1
            elif nums[i]*nums[i] < nums[j]*nums[j]:
                ans.append(nums[i]*nums[i])
                i -= 1
            else:
                ans.append(nums[j] * nums[j])
                j += 1
        return ans
        # 首先啊要两边都在哈
        # 全为正数
        # 全为负数

# 我找到了距离0最近的数字了吗？那我找绝对值最小的

nums = [-4,-1,0,3,10]
print(Solution.sortedSquares(Solution,nums))