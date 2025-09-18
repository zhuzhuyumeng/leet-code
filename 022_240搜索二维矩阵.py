class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        y_len = len(matrix)
        x_len = len(matrix[0])
        y=0
        x=x_len-1
        flag = False
        while flag==False:
            if matrix[y][x]<target: # 比目标值小，向下，补充向右
                y+=1
            if matrix[y][x]>target: # 比目标值大，向左，补充向上
                x-=1
            if matrix[y][x]==target:
                flag=True
                return flag

        return flag

nums = []


