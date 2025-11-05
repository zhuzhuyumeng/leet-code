class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        def backtracting(start:int,count: int):
            if count==0:
                res.append(tmp.copy())
                return
            if count<0:
                return
            for i in range(start,size):
                tmp.append(candidates[i])
                backtracting(i,count-candidates[i])
                tmp.pop()
# 我需要下一层不能前溯，如何
        start = 0
        size = len(candidates)
        res = []
        tmp = []
        backtracting(start,target)
        return res

if __name__ == '__main__':
    candidates = [2,3,6,7]
    target = 7
    soulution = Solution()
    res = soulution.combinationSum(candidates,target)
    print(res)