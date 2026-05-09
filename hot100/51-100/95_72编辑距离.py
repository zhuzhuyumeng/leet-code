class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m = len(word1) # m是word1
        n = len(word2) # n是word2
        dp = [[0 for i in range(m+1)]for j in range(n+1)]
        for i in range(m+1):
            dp[0][i] = i
        for i in range(n+1):
            dp[i][0] = i
        # 初始化每个单词对应另外一个空字符串所需要编辑的次数

        for i in range(1,n+1):
            for j in range(1,m+1):
                if word2[i-1] == word1[j-1]:
                    dp[i][j] = 1 + min(dp[i-1][j],dp[i][j-1],dp[i-1][j-1]-1)
                else:
                    dp[i][j] = 1 + min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1])

        return dp[n][m]

"""
转换字符word1变成word2，word1包含多少个word2已有的有序字符
1.dp数组以及下标的含义
dp[i][j]，A的前i个字符与B的前j个字符的结果
对于B的第j个字符，在A的末尾添加了一个字符所以有了+1，并非简单的数量关系
dp[i][j-1]，为什么dp[i][j]可以=min(dp[i][j-1]+1
2.递推公式
如果字母一致，只需要延续前面最小的结果，如果两个字符串都没有到这个位置，就-1抵消+1，如果一个达到了
如果不一致，最小结果再+1
if word1[j-1] == word2[i-1]
    dp[i][j] = min(dp[i-1][j],dp[i][j-1],dp[i-1][j-1])
else:
    dp[i][j] = 1 + min(dp[i-1][j],dp[i][j-1],dp[i-1][j-1])
5.举例推导
horse和ros
有两个相同顺序的字符，还有3个字符多，少一个字符r，检查字符的位置，之前有就可以省去重复删除插入
如何dp？
  0, h, o, r, s, e
  0, 1, 2, 3, 4, 5
r 1, 1, 2, 2, 3, 4
o 2, 2, 1, 2, 3, 4
s 3, 3, 2, 2, 2, 3
"""
if __name__ == "__main__":
    word1 = "horse"
    word2 = "ros"
    print(Solution.minDistance(Solution,word1,word2))