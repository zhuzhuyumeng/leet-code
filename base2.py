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
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        print()




if __name__ == "__main__":
    candidates = [10, 1, 2, 7, 6, 1, 5]
    target = 8
    with MemTimer():
        sol = Solution()
        res = sol.combinationSum2(candidates, target)
        print("结果:", res)