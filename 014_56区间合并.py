class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        intervals.sort(key=lambda p:p[0])
        ans = []
        for p in intervals:
            print(p[0])



intervals = [[1,3],[2,6],[8,10],[15,18]]
print(Solution.merge(Solution,intervals))
