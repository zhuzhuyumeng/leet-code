from typing import List
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        s_size = len(s)
        w_size = len(wordDict)
        dp = [False]*(s_size+1)
        dp[0] = True

        for i in range(1,s_size+1):
            # i遍历整个字符串标识
            for j in range(i):
                # j遍历单词，从头扫到位
                if s[j:i] in wordDict and dp[j]==True:
                    # 当这个位置前面的符合一个单词
                    dp[i]=True
        return dp[s_size]
"""
如何动态规划？需要单词字典wordDict把字符串s拼出来,
1.dp数组以及下标的含义
dp[j]表示容量为j的背包，能否被刚好装满？
2.递推公式

3.dp数组初始化
dp[s.size]，dp[0]=True，空字符串需要有表示

4.遍历顺序
那如何在遍历字符串的时候遍历单词组，正序遍历，无限个数
主要是字符串截取不会，substr()
5.举例推导
    l e e t c o d e
  0 1 2 3 4 5 6 7 8
  T F F F F F F F F
  T F F F T F F F T
  
"""

if __name__ == "__main__":
    s = "leetcode"
    wordDict = ["leet", "code"]
    print(Solution.wordBreak(Solution,s,wordDict))