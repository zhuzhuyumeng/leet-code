import time
import tracemalloc
from typing import List

class MemTimer:
    """上下文管理器：进入时开始计时、开始追踪内存；退出时打印耗时与峰值内存"""
    def __enter__(self):
        tracemalloc.start()          # 开始追踪
        self._t0 = time.perf_counter()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self._t1 = time.perf_counter()
        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()
        print(f"[MemTimer] 运行时间: {self._t1 - self._t0:.6f} s")
        print(f"[MemTimer] 峰值内存: {peak / 1024 / 1024:.3f} MB")   # 单位 MB

class Solution:
    def isPalindrome(self, start: int, end: int,s: str)->bool:
        j = end
        for i in range(start,end):
            if s[i]!=s[j]:
                return False
            j-=1
            if i < j:
                return True
        return True

    def partition(self, s: str) -> List[List[str]]:
        def backtracking(start:int):
            if start == size:
                res.append(path.copy())
                return
            for i in range(start,size):
                if self.isPalindrome(start,i,s):
                    tmp = ""
                    for j in range(start,i+1):
                        tmp += s[j]
                    path.append(tmp)
                    backtracking(i+1)
                    path.pop()

        res = []
        path = []
        size = len(s)
        backtracking(0)
        return res


# 切割完再进行回文子串的判别吗，如果在分割的时候做回文子串的判别，后续不符合的就不需要继续
# 回文串判别直接使用串的位置信息

if __name__ == "__main__":
    s = "efe"
    with MemTimer():
        sol = Solution()
        # res = sol.isPalindrome(s)
        res = sol.partition(s)
        print("结果:", res)
