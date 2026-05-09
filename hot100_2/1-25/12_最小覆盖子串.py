import sys
from itertools import count


class Solution:
    def minWindow(self,s:str,t:str) -> str:
        s_len = len(s)
        t_len = len(t)
        tmp = ""
        if s_len<t_len:
            return tmp
        need_cnt = {}
        for ch in t:
            need_cnt[ch] = need_cnt.get(ch,0)+1
        left = 0
        formed = 0
        ans = sys.maxsize
        # 通过标记来知道是否满足条件
        for right,ch in enumerate(s):
            if ch in need_cnt.keys():
                need_cnt[ch] -=1
                if need_cnt[s[right]]==0:
                    formed += 1
            # 直到满足条件，才开始缩小窗口
            while formed == len(need_cnt):
                # 如何比较最小值，因为需要记录left，不记录left，直接记录串
                if right-left+1<ans:
                    # 比最小值小就记录
                    tmp = s[left:right+1]
                ans = min(ans,right-left+1)
                if s[left] in need_cnt.keys():
                    need_cnt[s[left]] += 1
                    if need_cnt[s[left]] >0:
                        formed -= 1
                left+=1
        return tmp

"""
哈希表如何比较字符个数是否符合啊
"""

if __name__ == "__main__":
    s = "ADOBECODEBANC"
    t = "ABC"
    print(Solution.minWindow(Solution,s,t))