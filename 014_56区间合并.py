class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        intervals.sort(key=lambda p:p[0])
        ans = [] # 排序后的数组
        for p in intervals:
            if ans and p[0]<=ans[-1][1]: # 有在判断区间
                ans[-1][1] = max(ans[-1][1],p[1]) # 当前区间的尾数作为区间右尾数
            else:
                ans.append(p) #不在区间中，直接把这个加上去
        return ans

# intervals = [[1,3],[2,6],[8,10],[15,18]]
intervals = [[1,4],[2,3]]
print(Solution.merge(Solution,intervals))
