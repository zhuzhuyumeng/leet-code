from typing import List
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def backtracking(depth:int):
            if depth == size:
                res.append(tmp.copy())
                return
            for i in range(0,size):
                if nums[i] in used:
                    continue
                used.add(nums[i])
                tmp.append(nums[i])
                backtracking(depth+1)
                used.remove(nums[i])
                tmp.pop()

        res = []
        tmp = []
        depth = 0
        used = set()
        size = len(nums)
        backtracking(depth)
        return res


if __name__ == "__main__":
    nums = [1,2,3]
    sol = Solution()
    print(sol.permute(nums))