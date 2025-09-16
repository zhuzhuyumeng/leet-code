from collections import Counter, defaultdict


class Solution:
    def minWindow(self, s: str,t:str) -> str:
        # less用来标记是否子串字母全部符合，不符合，左端直接移动
        cnt = defaultdict(int)
        for c in t:
            cnt[c]+=1
        less = len(cnt) # 目标字母个数
        ansleft, ansright= -1, len(s)
        left = 0

        for right, c in enumerate(s):
            cnt[c]-=1
            if cnt[c]==0:
                less -=1
            while less ==0:
                if right - left < ansright - ansleft:
                    ansright = right
                    ansleft = left
                x = s[left] # 被移除窗口需要判断
                if cnt[x]==0:
                    less+=1
                cnt[x]+=1
                left+=1
        if ansleft==-1:
            return ""
        else:
            return s[ansleft: ansright+1]


s ="ADOBECODEBANC"
t= "ABC"
print(Solution.minWindow(Solution,s,t))
# 我的思路，创建一个hash用来放t字符串的字母集个数
# 另一个用来放s的滑动窗口的字母集个数，如果主集包含子集，覆盖
# 左窗口向右滑动直到不符合，右窗口继续滑动。
"""
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
return s[ansleft:ansright+1]# 原来是因为左闭右开吗

"""