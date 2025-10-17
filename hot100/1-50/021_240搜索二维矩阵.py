class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        y_len = len(matrix)
        x_len = len(matrix[0])
        y=0
        x=x_len-1
        flag = False
        while (y<y_len and x>=0):
            if matrix[y][x]==target:
                flag=True
                return flag
            if matrix[y][x]<target: # 比目标值小，向下，补充向右
                y+=1
            elif matrix[y][x]>target: # 比目标值大，向左，补充向上，此处非此即彼，不可以两个if否则会判断两次
                x-=1
        return flag

matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]
target = 155
print(Solution.searchMatrix(Solution,matrix,target))
"""
每行的元素从左到右升序排列。
每列的元素从上到下升序排列。
"""

