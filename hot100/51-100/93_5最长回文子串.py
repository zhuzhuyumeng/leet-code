class Solution:
    def isValidhuiwen(s: str)->int:
        n = len(s)
        for i in range(n):
            j = n-i-1
            if s[i]!=s[j]:
                return 0
            if j<i:
                break
        return 1

    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        dp = [[0 for i in range(n)]for i in range(n)]
        max_i_j = 0
        max_i = 0
        max_j = 0
        for i in range(n):
            for j in range(i,n):
                dp[i][j] = self.isValidhuiwen(s[i:j+1])
                # 这样子没有动态规划避免重复判断回文
                if dp[i][j]==1:
                    cur = j-i+1
                    if cur>max_i_j:#存在回文串
                        max_i_j = cur
                        max_i = i
                        max_j = j
        return s[max_i:max_j+1]
    def longestPalindromedp(self, s: str) -> str:
        n = len(s)
        if n<2:
            return s
        dp = [[0 for i in range(n)]for i in range(n)]
        for i in range(n):
            dp[i][i] = 1

        max_len = 1
        start = 0
        for length in range(2,n+1): # length控制字符间的间距
            for i in range(n-length+1): # i从0开始，在length长度之前
                j = i+length-1 #这步为什么j都在i的后面
                if s[i] == s[j]:
                    if length==2:
                        dp[i][j] = 1
                    else:
                        dp[i][j] = dp[i+1][j-1]
                if dp[i][j] and length>max_len:
                    max_len = length
                    start = i

        return s[start:start+max_len]
"""
每次判断两边的字符是否相等，再内部判断回文，有一种递归的感觉
区间dp
1.dp数组以及下标的含义
dp[i][j]表示字符串位置i到j是否为回文串
2.递推公式
if s[i] == s[j]:
    if length==2:
        dp[i][j] = 1
    else:
        dp[i][j] = dp[i+1][j-1]
3.dp初始化
全为0，对角线处为1，单个字符是字符串回文
4.遍历顺序
遍历长度从2到最大长度，i为字符串左边界，j为字符串右边界
i = (0, n-length+1)
j = (i + length -1)两个字母之间差为1
length = 2
i = 0
j = 0 + 2 -1
5.举例推导
  b a b a d
  0 1 2 3 4
0 1 0 1 0 0
1 0 1 0 1 0
2 0 0 1 0 0
3 0 0 0 1 0
4 0 0 0 0 1
"""

if __name__ == "__main__":
    s = "ac"
    print(Solution.longestPalindromedp(Solution,s))