class Solution:
    def placeZero(self,matrix:list[list[int]])->list[list[int]]:
        m = len(matrix[0])# 行
        n = len(matrix)# 列
        flag_col0 = 1
        flag_row0 = 1
        for i in range(n):
            if matrix[i][0]==0:
                flag_row0 = 0
        for j in range(m):
            if matrix[0][j]==0:
                flag_col0 = 0
        for i in range(1,n):
            for j in range(1,m):
                if matrix[i][j] == 0:
                    matrix[0][j] = 0
                    matrix[i][0] = 0
        for i in range(1,n):
            for j in range(1,m):
                if matrix[0][j] == 0 or matrix[i][0] == 0:
                    matrix[i][j]=0
        if flag_col0 == 0:
            for j in range(m):
                matrix[0][j]=0
        if flag_row0 == 0:
            for i in range(n):
                matrix[i][0]=0

        return matrix
"""
我只能想到复制出一个标识数组
然后按照那个数组中0的位置把原数组进行转换
直接第一行第一列都作为标记数组，用来标记该行或列
"""
if __name__ == "__main__":
    matrix = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
    print(Solution.placeZero(Solution,matrix))