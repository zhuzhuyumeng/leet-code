class Solution:
    def subsets(self,nums:list[int])->list[list[int]]:
        res = []
        path = []
        def dfs(start:int):
            res.append(path[:])

            for i in range(start,len(nums)):
                path.append(nums[i])
                dfs(i+1)
                path.pop()

        dfs(0)
        return res

"""
[
    [],
    [1],
    [1, 2],
    [1, 2, 3],
    [1, 3],
    [2],
    [2, 3],
    [3]
]
"""

if __name__ == "__main__":
    nums = [1,2,3]
    print(Solution.subsets(Solution,nums))