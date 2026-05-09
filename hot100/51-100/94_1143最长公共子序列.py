class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m = len(text1)
        n = len(text2)
        dp = [[0 for i in range(m+1)]for i in range(n+1)]
        for i in range(1,n+1):
            for j in range(1,m+1):
                if text1[j-1] == text2[i-1]:
                    dp[i][j] = dp[i-1][j-1]+1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        return dp[n][m]

"""
最长的顺序一致的子字符串
如何存在动态转移，以较长的字符串为dp
使用较短字符串进行匹配
两个字符串的长短不做判断吗？创造出的二维数组不是有区别嘛
1.dp数组以及下标的含义
dp[i][j]表示两个字符串，i到j字符存在的公共字符的个数
2.递推关系
当前两个字符相等，就可以在两个少一个字符串的基础上+1
如果不等就从各字符串少一个继承最大值
if text1[m] == text2[n]:
    dp[i][j] = dp[i-1][j-1]+1
else:
    dp[i][j] = max(dp[i-1][j],dp[i][j-1])
5.举例说明
  0, a, b, c, a, e
  0, 0, 0, 0, 0, 0
a 0, 1, 1, 1, 1, 1
c 0, 1, 1, 2, 2, 2
e 0, 1, 1, 2, 2, 3
"""

if __name__ == "__main__":
    text1 = "abcde"
    text2 = "ace"
    print(Solution.longestCommonSubsequence(Solution,text1,text2))