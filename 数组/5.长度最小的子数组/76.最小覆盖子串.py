import sys
from collections import Counter
from xmlrpc.client import MAXINT


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        s_size = len(s)
        t_size = len(t)
        tmp = ""
        if s_size<t_size:
            return tmp

        left= 0
        ans = sys.maxsize

        need_cnt = {}
        for i, num in enumerate(t):
            need_cnt[num] = need_cnt.get(num,0)+1
        required = len(need_cnt)
        formed=0 # 已经满足的字符串种类
        for right, ch in enumerate(s):
            # 我如何检查cnt[t]是否全为0
            if ch in need_cnt:
                need_cnt[ch] -= 1
                if need_cnt[ch] == 0:
                    formed+=1
            while formed==required:
                if right-left+1 < ans:
                    # for i in range(left,right+1):
                    tmp = s[left:right+1]
                ans = min(ans,right-left+1)
                #处理left,在需要中，不再需要中
                if s[left] in need_cnt:
                    need_cnt[s[left]] += 1
                    if need_cnt[s[left]] > 0:
                        formed -= 1
                left+=1
        return tmp



# 哈希表如何动态维护？
# 左右指针如何维护
s = "ADOBECODEBANC"
t = "ABC"
print(Solution.minWindow(Solution,s ,t ))
