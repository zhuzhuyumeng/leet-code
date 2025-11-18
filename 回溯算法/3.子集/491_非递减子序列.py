from typing import List
class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        def backtracking(startindex: int):
            if startindex>size:
                return
            if len(tmp)>1:
                res.append(tmp.copy())
            used = set()
            for i in range(startindex,size):
                if (len(tmp)>0 and nums[i]<tmp[-1]) or nums[i] in used: # 当前数字比最后一个数字小，就不加入
                    continue
                used.add(nums[i])
                tmp.append(nums[i])
                backtracking(i+1)
                tmp.pop()
        res = []
        tmp = []
        size = len(nums)
        backtracking(0)
        return res


if __name__ == "__main__":
    nums = [1,2,3,1,1,1,1]
    sol = Solution()
    print(sol.findSubsequences(nums))