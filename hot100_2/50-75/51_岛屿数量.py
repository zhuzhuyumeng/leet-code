from collections import deque


class Solution:

    def numIslands(self, grid: list[list[str]]) -> int:
        # 深度优先搜索，进入递归注意修改数值防止无限递归，纯循环扫无变化
        def dfs(grid: list[list[str]], i, j):
            grid[i][j] = '0'
            directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
            for dx, dy in directions:
                y = i+dy
                x = j+dx
                if 0 <= i+dy < n and 0<= j+dx <m:# 在界内
                    if grid[i+dy][j+dx] =='1':
                        dfs(grid,i+dy,j+dx)
            return

        res = 0
        m = len(grid[0])
        n = len(grid)
        for i in range(n):
            for j in range(m):
                # print(grid[i][j])
                if grid[i][j] == '1':
                    res +=1

                    dfs(grid, i, j)
        return res

    def numIslands2(self, grid: list[list[str]]) -> int:
        def bfs(grid: list[list[str]], i, j):
            queue = deque()
            queue.append((i,j))
            grid[i][j] = '0'
            directions = [(1,0),(0,1),(-1,0),(0,-1)]
            while queue:
                cur_i,cur_j = queue.popleft()
                for dx,dy in directions:
                    x = cur_j+dx
                    y = cur_i+dy
                    if 0<= x < m and 0<= y <n and grid[y][x]=='1':
                        queue.append((y,x))
                        grid[y][x] = '0'

        res = 0
        m = len(grid[0])
        n = len(grid)
        for i in range(n):
            for j in range(m):
                # print(grid[i][j])
                if grid[i][j] == '1':
                    res += 1
                    bfs(grid, i, j)
        return res


if __name__ == "__main__":
    grid = [
        ['1', '1', '1', '1', '0'],
        ['1', '1', '0', '1', '0'],
        ['1', '1', '0', '0', '0'],
        ['0', '0', '0', '0', '0']
    ]
    print(Solution.numIslands2(Solution,grid))

"""
从左上开始，遍历，有岛屿就，左右上下下，遍历过赋值为遍历过，
怎么做三方向的，哦存在四方向的情况
"""