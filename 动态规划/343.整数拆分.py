from typing import List
class Solution:
    def integerBreak(self, n: int) -> int:
        dp = [0]*(n+1)
        dp[1] = 1
        dp[2] = 1
        for i in range(3,n+1):
            for j in range(1,(i+2)//2): # //2是为了不重复计算，比如1、3和3、1
                dp[i] = max(max(j*(i-j),j*dp[i-j]),dp[i])
                #第一个max是比较后的数字，里面的max是两个数字比较多个数字（拆分），比如6和其中的3,3
                print(f"dp[{i}]",dp[i])
                print("----------------")
        return dp[n]
# DP数组含义，数字个数不确定
# DP推导公式
# DP数组初始化
# 遍历出DP
# 举例DP

if __name__ =="__main__":
    n = 7
    sol = Solution()
    print(sol.integerBreak(n))