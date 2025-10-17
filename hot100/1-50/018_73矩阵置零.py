class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # 先纵后横
        m = len(matrix) # y轴长度
        n = len(matrix[0]) # x轴长度
        new = [[1 for _ in range(n)] for _ in range(m)]
        for y in range(m):
            for x in range(n):
                if matrix[y][x]==0:
                    new[y][x]=0
        for y in range(m):
            for x in range(n):
                if new[y][x]==0:
                    for i in range(n):
                        matrix[y][i]=0
                    for j in range(m):
                        matrix[j][x]=0
        print(matrix)

matrix = [[1,1,1],[1,0,1],[1,1,1]]
print(Solution.setZeroes(Solution,matrix))
