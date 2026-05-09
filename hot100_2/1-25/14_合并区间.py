class Solution:
    def merge(self,intervals:list[list[int]]) -> list[list[int]]:
        ans = list()
        intervals.sort()
        ans.append(intervals[0])
        n = len(intervals)
        for i in range(1,n):
            num =  ans.pop()
            left = num[0]
            right = num[1]
            if intervals[i][0]<=right: # 后左比前右小等
                if intervals[i][1]>right:
                    ans.append([left,intervals[i][1]])
                else: # 后右边界比前右边界小
                    ans.append([left,right])
            else:
                ans.append(num)
                ans.append(intervals[i])
        return ans
    def merge2(self,intervals:list[list[int]]) -> list[list[int]]:
        ans = list()
        intervals.sort()
        ans.append(intervals[0])
        for i in range(1,len(intervals)):
            if intervals[i][0] > ans[-1][1]: # 超过右边界
                ans.append(intervals[i])
            elif intervals[i][0] <= ans[-1][1]: # 有交集
                if intervals[i][1] > ans[-1][1]: # 后面一个右边界大，改大右边界，不大不管
                    ans[- 1][1] = intervals[i][1]
        return ans



if __name__ == "__main__":
    intervals = [[1,3],[2,6],[8,10],[15,18]]
    print(Solution.merge2(Solution,intervals))