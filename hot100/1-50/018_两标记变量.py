class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # 先纵后横
        m = len(matrix) # y轴长度
        n = len(matrix[0]) # x轴长度
        flag_col0 = [1 for _ in range(m)]# 列
        for i in range(m):
            if matrix[i][0]==0:
                flag_col0[i]=0

        flag_row0 = [1 for _ in range(n)]
        for i in range(n):
            if matrix[0][i]==0:
                flag_row0[i]=0
        # print(flag_row0)
        for y in range(1,m):
            for x in range(1,n):
                if matrix[y][x]==0:
                    matrix[y][0] = 0
                    matrix[0][x] = 0
        for y in range(1,m):
            for x in range(1,n):
                if matrix[y][0]==0 or matrix[0][x]==0:
                    matrix[y][x]=0

        for y in range(m): # y遍历，取位置
            if flag_col0[y]==0:
                for x in range(n):
                    matrix[y][x] = 0 # 横给值
                for j in range(m):
                    matrix[j][0] = 0 #

        for x in range(n):
            if flag_row0[x]==0:
                for y in range(m):
                    matrix[y][x] = 0
                for x in range(n):
                    matrix[0][x] = 0
        print(matrix)

# matrix = [[1,1,1],[1,0,1],[1,1,1]]
# matrix = [[1,0,1]]
matrix = [[1,2,3,4],[5,0,7,8],[0,10,11,12],[13,14,15,0]]
print(Solution.setZeroes(Solution,matrix))
