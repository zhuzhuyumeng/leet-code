import sys
from typing import List
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        pre= 1
        bck = 1
        ans = -sys.maxsize
        for i in range(n):
            j = n-1-i
            pre *= nums[i]
            bck *= nums[j]
            ans = max(max(ans,nums[i]),max(pre,bck))
            if nums[i]==0: # 遇到0前缀重置，在下一个位置生效
                pre=1
            if nums[j]==0: # 遇到0后缀重置，在下一个位置生效
                bck=1
        return ans

"""
这题需要最大的连续非空子数组，所以要用倒序？0要特殊解决
当前位置的最优解未必是前一个位置的最优解转移得到的
前缀积的方法不合适，用双向前缀积，遇到0归零
答案区间的一端必定是0或数组起终点
3.初始化

4.遍历顺序

5.举例推导
   2 3 -2   4
   0 1  2   3  
   2 6 -12 -48
   2 
"""
if __name__ == "__main__":
    nums = [2,3,-2,4]
    nums = [-2]
    print(Solution.maxProduct(Solution,nums))
