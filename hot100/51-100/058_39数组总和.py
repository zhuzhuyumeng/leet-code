class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        def dfs(start:int,target:int,path:list[int],res:list[list[int]]):
            if target==0:
                res.append(path.copy())
                return
            for i in range(start,size):
                target -= candidates[i]
                if target<0:
                    return
                path.append(candidates[i])
                dfs(i,target,path,res)# 前面遍历过了，大数就不加入小数了
                target += candidates[i]
                path.pop()

        res = []
        candidates.sort()
        size = len(candidates)
        start = 0
        path = []
        dfs(start,target,path,res)
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