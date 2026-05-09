from typing import List
class Solution:
    def findTargetSumWays(self,nums:List[int],target:int)->int:
        total = sum(nums)
        if (total-target)%2:#是偶数，才可以给两个数组分啊
            return 1
        n = len(nums)
        dp = [0]*(total+1)
        dp[0] = 1

        for j,num in enumerate(nums):
            for i in range(total,-1,-1):
                if num<=i:
                    if dp[i]|dp[i-num]:
                        dp[i] = (dp[i]|dp[i-num])+1
                    else:
                        dp[i] = dp[i]
                else:
                    dp[i] = dp[i]

        return dp[target]

# 我真的爱用可达性，还是没有理解，这个不好统计数量啊

"""
        def backtracking(nums:List[int],index:int,target:int):
            if target==0 and index==sizes:
                res.append(tmp.copy())
                return
            if index==sizes:
                return
            else:
                for i,sign in enumerate(signs):
                    tmp.append(nums[index])
                    backtracking(nums,index+1,target+sign*nums[index])
                    tmp.pop()

        sizes = len(nums)
        signs = [-1,1]
        res = []
        tmp = []
        index = 0
        backtracking(nums,index,target)
        return len(res)
"""

"""
数量搜满了，数量没搜满
既然总是要求和的，那就以几个数的和为基准，动态规划是否减去那个数
1.dp数组以及下标的含义
dp[j]表示这个价值能被达到几次
2.递推公式

3.dp数组初始化

4.遍历顺序

5.举例

"""

if __name__ == "__main__":
    nums = [1, 1, 1, 1, 1]
    # nums = [11,19,14,50,47,35,18,32,8,2,31,45,6,25,49,23,25,33,24,33]
    nums = [1,3,6]
    target = 3
    print(Solution.findTargetSumWays(Solution, nums,target))