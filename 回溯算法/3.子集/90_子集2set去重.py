from typing import List
class Solution:
    def subsets2(self, nums: List[int]) -> List[List[int]]:
        def backtracking(startindex: int):
            if startindex>size:
                return
            res.append(tmp.copy())
            used = set()

            for i in range(startindex,size):
                if nums[i] in used: #如果被使用过就跳过
                    continue
                used.add(nums[i])# 为什么不要remove啊
                tmp.append(nums[i])
                backtracking(i+1)
                tmp.pop()

        res = []
        tmp = []
        size = len(nums)
        backtracking(0)
        return res


if __name__ == "__main__":
    nums = [1,2,2]
    sol = Solution()

    print(sol.subsets2(nums))