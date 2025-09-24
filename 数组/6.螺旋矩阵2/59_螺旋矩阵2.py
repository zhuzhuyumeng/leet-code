class Solution:
    def generateMatrix(self, n: int) -> list[list[int]]:
        total = n*n
        DIRS = [0,1],[1,0],[0,-1],[-1,0] # 右、下、左、上
        matrix = [[0 for _ in range(n)] for _ in range(n)]
        i = 0
        j = 0
        k=1
        cur = 0
        for _ in range(total):
            # 第一个数字
            matrix[i][j] = k
            k += 1
            # 看下一个位置
            x = i + DIRS[cur][0]
            y = j + DIRS[cur][1]
            if x<0 or x>=n or y<0 or y>=n or matrix[x][y] != 0:
                cur +=1
            cur = cur%4# 四个方向牢底
            i = i+DIRS[cur][0]
            j = j+DIRS[cur][1]
        print(matrix)

n = 3
Solution.generateMatrix(Solution,n)