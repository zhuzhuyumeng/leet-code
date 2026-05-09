class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        def dfs(depth,visited:list[bool],res:list[int]):
            if depth == n:
                path.append(res.copy())
            for i in range(n):
                if visited[i] == False:# 没遍历过
                    visited[i] = True
                    res.append(nums[i])
                    dfs(depth+1,visited,res)
                    visited[i] = False
                    res.pop()

        n = len(nums)
        visited = [False] * n # 个数
        path = []
        depth = 0
        res = []
        dfs(depth,visited,res)
        return path



if __name__ == '__main__':
    nums = [1,2,3]
    solution = Solution()
    res = solution.permute(nums)
    print(res)


