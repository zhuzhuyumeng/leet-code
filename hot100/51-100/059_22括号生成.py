class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        def backtracking(n:int,res: list[str],left: int,right: int,str: str):
            if right>left:
                return
            if left == right ==n:
                res.append(str)
                return
            if left<n:
                backtracking(n, res, left+1, right, str+"(")
            if right<left:
                backtracking(n, res, left, right+1, str+")")



        res = []
        backtracking(n,res,0,0,"")
        return res



if __name__ == '__main__':
    n = 3
    solution = Solution()
    res = solution.generateParenthesis(n)
    print(res)

"""
在任何情况下，左括号应该比右边的多
"""