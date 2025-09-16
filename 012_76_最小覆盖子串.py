from collections import Counter


class Solution:
    def minWindow(self, s: str,t:str) -> str:
        n = len(s)
        ansleft = -1
        ansright = n
        cnt_s = Counter()
        cnt_t = Counter(t)
        left = 0
        for right,c in enumerate(s):
            cnt_s[c] +=1
            while cnt_s >= cnt_t:
                if right-left < ansright-ansleft:
                    ansright = right
                    ansleft = left
                cnt_s[s[left]]-=1
                left+=1
        return s[ansleft,ansright+1]


s ="ADOBECODEBANC"
t= "ABC"
print(Solution.minWindow(Solution,s,t))
# 我的思路，创建一个hash用来放t字符串的字母集个数
# 另一个用来放s的滑动窗口的字母集个数，如果主集包含子集，覆盖
# 左窗口向右滑动直到不符合，右窗口继续滑动。