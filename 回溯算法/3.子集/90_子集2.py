from typing import List
class Solution:
    def subsets2(self, nums: List[int]) -> List[List[int]]:
        def backtracking(startindex: int):
            if startindex>size:
                return
            res.append(tmp.copy())
            for i in range(startindex,size):
                if i>startindex and nums[i]==nums[i-1]:
                    continue
                tmp.append(nums[i])
                backtracking(i+1)
                tmp.pop()

        res = []
        tmp = []
        size = len(nums)
        backtracking(0)
        return res


if __name__ == "__main__":
    nums = [4,4,4,1,4]
    nums.sort()
    sol = Solution()

    print(sol.subsets2(nums))