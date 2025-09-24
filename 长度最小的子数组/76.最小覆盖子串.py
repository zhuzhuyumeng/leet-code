from collections import Counter
from xmlrpc.client import MAXINT


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s)<len(t):
            return ""
        s_size = len(s)
        t_size = len(t)
        left = 0
        right = 0
        for left in range(0,s_size):
            sum = MAXINT
            print(sum)




# 哈希表如何动态维护？
# 左右指针如何维护
s = "ADOBECODEBANC"
t = "ABC"
print(Solution.minWindow(Solution,s ,t ))
