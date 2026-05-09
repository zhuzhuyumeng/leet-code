from typing import List
class Solution:
    def find_maxvalue(self,weight:List[int],value:List[int],bigweight:int):
        m = len(weight)
        n = bigweight
        dp =[[0]*(n+1) for _ in range(m)] # dp是靠左上和上赋值的，初始化不挑
        for i in range(m): # 容量为0，竖着全为0
            dp[i][0] = 0
        maxvalue = 0
        for j in range(n+1): # 第一排
            if weight[0]<=j: # 第一个物品重量小于等于容积，赋予该物品的价值
                dp[0][j] = value[0]
                maxvalue = max(maxvalue, dp[0][j])
            else:
                dp[0][j] = 0
        # print(dp)
        for i in range(1,m):
            for j in range(1,n+1):
                if j-weight[i]>=0: # 重量能放的下
                    dp[i][j] = max(dp[i-1][j],dp[i-1][j-weight[i]]+value[i])
                else: # 放不下需要用上面的值
                    dp[i][j] = dp[i-1][j]
                maxvalue = max(maxvalue,dp[i][j])
        print(dp)
        return maxvalue

            # dp二维数组如何表示空间，价值

if __name__ == "__main__":
    bigweight = 6
    weight = [2,2,3,1,5,2]
    value = [2,3,1,5,4,3]
    # # 第一行：M 种物品，背包容量 N
    # M, k = map(int, input().split())
    # # 第二行：每种物品的体积（长度=M）
    # weight = list(map(int, input().split()))
    # # 第三行：每种物品的价值（长度=M）
    # value = list(map(int, input().split()))
    sol = Solution()
    print(sol.find_maxvalue(weight,value,bigweight))
"""
6 1
2 2 3 1 5 2
2 3 1 5 4 3
"""
