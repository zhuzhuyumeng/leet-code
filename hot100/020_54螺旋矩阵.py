class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        y_len = len(matrix) # y
        x_len = len(matrix[0]) # x
        # 通过方向数组进行旋转
        # 向右(0,1),向下(0
        DIRS = (0,1),(1,0),(0,-1),(-1,0)
        print(DIRS[0][1])
        total = x_len*y_len
        ans = []
        i = j = di = 0
        for _ in range(total):
            ans.append(matrix[i][j])
            matrix[i][j] = None
            x,y = i+DIRS[di][0],j+DIRS[di][1]
            if x<0 or x>= y_len or y<0 or y>=x_len or matrix[x][y]==None:
                di = (di+1)%4
            i = i+DIRS[di][0]
            j = j+DIRS[di][1]
        return ans


matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
print(Solution.spiralOrder(Solution,matrix))

"""
1  2  3  4
5  6  7  8
9 10 11 12
"""