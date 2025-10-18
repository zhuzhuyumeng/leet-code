class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        def dfs(start:int):
            res.append(path.copy())
            for i in range(start,len(nums)):
                path.append(nums[i])
                dfs(i+1)
                path.pop()
        # 对每个数字后面进行枚举
        res = []
        path = []
        start = 0
        dfs(start)
        return res



if __name__ == '__main__':
    nums = [1,2,3]
    solution = Solution()
    res = solution.subsets(nums)
    print(res)