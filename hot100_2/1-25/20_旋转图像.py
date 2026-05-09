class Solution:
    def roate(self, matrix: list[list[int]]) -> list[int]:
        m = len(matrix[0])
        n = len(matrix)
        # 水平翻转
        for i in range(int(n/2)):
            for j in range(m):
                matrix[i][j],matrix[n-1-i][j] = matrix[n-1-i][j],matrix[i][j]
        # print(matrix)
        for i in range(n):
            for j in range(i,m):
                matrix[i][j],matrix[j][i] = matrix[j][i],matrix[i][j]
        # print(matrix)

"""
原地旋转，不可以新建矩阵
固定纵坐标，变化横坐标。旋转位置后就是固定横坐标，变化纵坐标，对应关系是对称的
水平线翻转+左对角线翻转
"""
if __name__ == "__main__":
    matrix = [[1,2,3],[4,5,6],[7,8,9]]
    matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
    print(Solution.roate(Solution,matrix))