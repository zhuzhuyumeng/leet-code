import collections
from collections import deque
from typing import Deque


class Solution:
    def isValid(self, s: str) -> bool:
        deque = collections.deque()
        size = len(s)
        num = 0
        for i in range(0,size):
            if s[i]=="(" or s[i]=="{" or s[i]=="[":
                a = s[i]
                deque.append(a)
                num+=1

            elif s[i]==")":
                num -= 1
                if num <0 or deque.pop() != "(":
                    return False
            elif s[i] == "}":
                num -= 1
                if num <0 or deque.pop() != "{":
                    return False
            elif s[i] == "]":
                num -= 1
                if num < 0 or deque.pop() != "[":
                    return False

        if num!=0:
            return False
        return True

if __name__ == "__main__":
    s = ")"
    # s = "()[]{}"
    sol = Solution()
    print(sol.isValid(s))