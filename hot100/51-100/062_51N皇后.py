from typing import List
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def backtracking(depth:int):
            if depth==n:
                tmp = []
                for y in range(len(qipan)):
                    s = ''
                    for x in range(len(qipan[0])):
                        s += qipan[y][x]
                    tmp.append(s)
                res.append(tmp)
                return

            for i in range(n):
                if i in shu or depth-i in left or depth+i in right:
                    continue
                qipan[depth][i]="Q"
                left.append(depth - i)
                right.append(depth + i)
                shu.append(i)
                backtracking(depth+1)
                qipan[depth][i] = "."
                left.remove(depth - i)
                right.remove(depth + i)
                shu.remove(i)



        res = []
        qipan = [["." for i in range(n)] for i in range(n)]
        left = []
        right = []
        shu = []
        backtracking(0)
        return res

if __name__ == "__main__":
    n = 4
    sol = Solution()
    print(sol.solveNQueens(n))