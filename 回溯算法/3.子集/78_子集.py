from typing import List
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def backtracking(start:int,depth:int):
            # if depth<=size:
            #     res.append(tmp.copy())
            # if depth> size:
            #     return
            if start>size:
                return
            res.append(tmp.copy())
            for i in range(start,size):
                tmp.append(nums[i])
                backtracking(i+1,depth+1)
                tmp.pop()
        res = []
        tmp = []
        size = len(nums)
        depth = 0
        backtracking(0,0)
        return res

if __name__ == "__main__":
    nums = [1, 2, 3]
    sol = Solution()

    print(sol.subsets(nums))