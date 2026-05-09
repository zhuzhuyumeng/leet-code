class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = []
        n = len(s)
        num = [1]*n
        tag = -1
        for i,ch in enumerate(s):
            if ch=='(':
                stack.append(i)
                # 存索引要比存字符更有意义，索引不仅可以进行字符串对比，还可以直接用于标记数组，
            elif ch==')':
                if stack:
                    pre_index = stack.pop()
                    end_ch = s[pre_index]
                    if end_ch == '(':# 这里应该是下标，而不是前面一位
                        num[pre_index] = 0
                        num[i] = 0

        print(num)
        max_length = 0
        tmp = 0
        for i,num in enumerate(num):
            if num==0:
                tmp += 1
                max_length = max(max_length,tmp)
            elif num==1:
                tmp = 0

        return max_length

    def longestValidParenthesesdp(self, s: str) -> int:
        n = len(s)
        dp = [0]*n
        for i in range(n):
            if s[i]==")" and i-dp[i-1]-1>=0:
                dp[i]=2+dp[i-1]+dp[i-dp[i-1]-2]
        return dp[n-1]

"""
不能通过一个辅助数字来实现对称消除
1 1 1 1 1 1
1 0 0 1 1 1
1 0 0 0 0 1
如何动态规划、状态转移
1.dp数组以及下标的含义
"""
if __name__ == "__main__":
    s = "()(())"
    s = "(()())"
    print(Solution.longestValidParenthesesdp(Solution,s))