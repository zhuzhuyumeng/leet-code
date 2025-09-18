class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        y_len = len(matrix)
        x_len = len(matrix[0])
        y=0
        x=x_len-1
        flag = False
        while flag==False:
            if matrix[y][x]




