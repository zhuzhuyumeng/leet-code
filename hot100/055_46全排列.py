class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        def dfs(nums,size,depth,path,visited,res):
            if depth == size:
                res.append(path.copy())
                return
            for i in range(size):
                if visited[i] is False: # visited是按照数字在列表的位置来排的，不用担心
                    path.append(nums[i])
                    visited[i]=True
                    depth+=1
                    dfs(nums,size,depth,path,visited,res)
                    depth-=1
                    visited[i]=False
                    path.pop()

        size = len(nums)
        path = []
        depth = 0
        if size==0:
            return 0
        res = []
        visited = [False for _ in range(size)]
        dfs(nums,size,depth,path,visited,res)
        return res
if __name__ == '__main__':
    nums = [1,2,3]
    solution = Solution()
    res = solution.permute(nums)
    print(res)


"""
[1,2,3]
长度，排列组合，标记列表
"""