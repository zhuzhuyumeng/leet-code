from typing import List
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def backtracking(depth:int):
            if depth == size:
                tmp = []
                for y in range(len(qipan)):
                    s = ''
                    for x in range(len(qipan[0])):
                        s += qipan[y][x]
                    tmp.append(s)
                res.append(tmp)
                return

            for i in range(0,size):
                wi = i
                wd = depth
                found = False
                while wi-1>-1 and wd -1 >= -1: # 左上
                    wi -= 1
                    wd -= 1
                    if qipan[wd][wi]=='Q':
                        found = True

                if found:
                    continue
                wi = i
                wd = depth
                while wi + 1 <= size-1 and wd - 1 >= -1: # 右上
                    wi += 1
                    wd -= 1
                    if qipan[wd][wi] == 'Q':
                        found = True
                if found:
                    continue
                for y in range(0,depth):
                    if qipan[y][i] == 'Q':
                        found = True
                        continue
                if found:
                    continue
                qipan[depth][i] = 'Q'
                backtracking(depth+1)
                qipan[depth][i] = '.'

        size = n
        res = []
        qipan = [['.' for i in range(n)]for i in range(n)]
        backtracking(0)
        return res
# 你可以尝试放置一个皇后，固定他的影响，后面在影响中搜索是否被影响。

if __name__ == "__main__":
    n = 4
    sol = Solution()
    print(sol.solveNQueens(n))