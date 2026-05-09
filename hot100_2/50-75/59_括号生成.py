class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        def dfs(left,right,path):
            if left<right:
                return
            if left == right ==n:
                res.append(path)
                return
            if left >n or right>n:
                return
            dfs(left+1,right,path+'(')
            dfs(left, right+1, path + ')')
            # 会走到非法空间
        def dfs2(left,right,path):
            if len(path) == 2*n:
                res.append(path)
                return
            if left<n:
                dfs(left + 1, right, path + '(')
            if right<left:
                dfs(left, right + 1, path + ')')

        res = []
        path = ""
        dfs(0,0,path)
        return res

if __name__ == '__main__':
    n = 3
    solution = Solution()
    res = solution.generateParenthesis(n)
    print(res)

"""
在任何情况下，左括号应该比右边的多
"""