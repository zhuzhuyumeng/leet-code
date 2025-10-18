class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        def dfs(depth:int,path:str):
            if n-depth == 0:
                res.append(path)
                return
            for i in range(depth,size):
                dfs(depth+1,path+'(')
                path = path + ')'

        res = []
        size = n
        path=""
        depth = 0
        dfs(depth,path)
        return res


if __name__ == '__main__':
    n = 1
    solution = Solution()
    res = solution.generateParenthesis(n)
    print(res)