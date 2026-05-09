"""
import time
import tracemalloc
from typing import List

class MemTimer:
    # 上下文管理器：进入时开始计时、开始追踪内存；退出时打印耗时与峰值内存
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
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        def backtracting(start:int,count: int):
            if count==0:
                res.append(tmp.copy())
                return
            if count<0:
                return
            for i in range(start,size):
                if count-candidates[i]<0:
                    break
                tmp.append(candidates[i])
                backtracting(i,count-candidates[i])
                tmp.pop()
# 我需要下一层不能前溯，如何
        start = 0
        size = len(candidates)
        res = []
        tmp = []
        candidates.sort()
        backtracting(start,target)
        return res

if __name__ == '__main__':
    candidates = [2,3,6,7]
    target = 7
    with MemTimer():
        sol = Solution()
        ans = sol.combinationSum(candidates, target)
        print("结果:", ans)
"""

from typing import List
class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        def backtracking(candidates: list[int],index:int,target: int):
            if target==0: #符合条件退出一层
                res.append(tmp.copy())
                return
            if target<0: #超过条件，退出两层
                return
            elif target>0: #不符合条件
                for i in range(index,size):
                    tmp.append(candidates[i])
                    backtracking(candidates,i, target-candidates[i])
                    tmp.pop()

        size = len(candidates)
        res = [] # 存放结果的数组
        tmp = []
        index = 0
        candidates.sort()
        backtracking(candidates,index,target)
        return res

"""
2
[2,3,6,7]
2,2
3,6,7]
2,2,2
3,6,7]
有点像完全背包问题
"""
if __name__ == '__main__':
    candidates = [2,3,6,7]
    target = 7
    sol = Solution()
    ans = sol.combinationSum(candidates, target)
    print("结果:", ans)