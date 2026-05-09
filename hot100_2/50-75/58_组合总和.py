class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        def dfs(start,candidates,path,target):
            if target==0:
                res.append(path[:])
                return
            if target<0:
                return
            if target>0:
                for i in range(start,len(candidates)):
                    if candidates[i]> target:
                        break
                    path.append(candidates[i])
                    dfs(i,candidates,path,target-candidates[i])
                    path.pop()
        res = []
        path = []
        candidates.sort()
        dfs(0,candidates,path,target)
        return res

"""
如何去除重复，而不是之后再排序去重
"""



if __name__ == '__main__':
    candidates = [2,3,6,7]
    target = 7
    solution = Solution()
    res = solution.combinationSum(candidates,target)
    print(res)