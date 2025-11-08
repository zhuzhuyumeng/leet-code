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
    def restoreIpAddresses(self, s: str) -> List[str]:
        def backtracking(start:int,depth: int):
            if start==size and depth ==4:
                tmp =''
                for i in range(0,4):
                    tmp+= path[i]+'.'
                tmp = tmp[:-1]
                res.append(tmp)
                return
            for i in range(start,size):
                if i - start ==3:
                    break
                tmp = ''
                for j in range(start,i+1):
                    tmp += s[j]
                if int(tmp)>255:
                    break
                if len(tmp)>1 and tmp[0]=='0':
                    break
                path.append(tmp)
                backtracking(i+1,depth+1)
                path.pop()

        res = []
        size = len(s)
        path = []
        depth = 0
        backtracking(0,depth)
        return res
# 应该先切割，再拼起来
if __name__ == "__main__":
    # s = "25525511135"
    s = "010010"
    with MemTimer():
        sol = Solution()
        res = sol.restoreIpAddresses(s)
        print("结果:", res)
