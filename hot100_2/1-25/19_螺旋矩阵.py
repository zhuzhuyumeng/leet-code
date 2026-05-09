class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        m = len(matrix[0])
        n = len(matrix)
        ans = []
        direction = [[0,1],[1,0],[0,-1],[-1,0]]
        di = 0
        i,j = 0,0
        total = m*n
        index = 0
        while index<total:
            ans.append(matrix[i][j])
            matrix[i][j] = -100
            x = i + direction[di][0]
            y = j + direction[di][1]
            # 新建一个变量进行判断，我真傻啊
            if x>=n or y >=m or matrix[x][y]==-100:
                di = (di+1)%4
            i = i + direction[di][0]
            j = j + direction[di][1]
            index+=1

        return ans
    def spiralOrder2(self, matrix: list[list[int]]) -> list[int]:
        m = len(matrix[0])
        n = len(matrix)
        direction = [[0,1],[1,0],[0,-1],[-1,0]]
        total = m * n
        index = 0
        rst = []
        i,j = 0,0
        k=0
        while index<total:
            rst.append(matrix[i][j])
            matrix[i][j] = -100 # 走过了
            x = j+direction[k][1]
            y = i+direction[k][0]
            if x>=m or x<0 or y>=n or y<0 or matrix[y][x]==-100:
                k= (k + 1)%4
                x = j + direction[k][1]
                y = i + direction[k][0]
            i = y
            j = x
            index += 1
            # 赋值了
        return rst


if __name__ == "__main__":
    matrix = [[1,2,3],[4,5,6],[7,8,9]]
    print(Solution.spiralOrder2(Solution,matrix))