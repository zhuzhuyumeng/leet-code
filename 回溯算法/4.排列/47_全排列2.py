from typing import List
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        def backtracking(depth:int):
            if depth == size:
                res.append(tmp.copy())
                return
            for i in range(0,size):
                if used[i]==True:
                    continue
                if i>0 and nums[i] == nums[i-1] and used[i-1] == False: # 达到第二个1，前两个条件，我不是第一次出现的数字。第三个条件，前面的数字已经排列过了。
                    continue
                used[i] = True
                tmp.append(nums[i])
                backtracking(depth+1)
                used[i] = False
                tmp.pop()

        res = []
        tmp = []
        depth = 0
        size = len(nums)
        used = [False] * size
        nums.sort()
        backtracking(depth)
        return res


if __name__ == "__main__":
    nums = [1,1,2]
    sol = Solution()
    print(sol.permuteUnique(nums))