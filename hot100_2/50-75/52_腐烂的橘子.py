import collections
from collections import deque

class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:
        def bfs(grid: list[list[int]],i,j):
            directions = [(1,0),(0,1),(-1,0),(0,-1)]
            for dx,dy in directions:
                x = j + dx
                y = i + dy
                if 0<=x<m and 0<=y<n and grid[y][x]==1:
                    # 入队标记腐烂
                    grid[y][x] = 2
                    queue.append((y,x))
            return

        m = len(grid[0])
        n = len(grid)
        res = 0
        queue = collections.deque()
        # 找烂橘子
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 2:
                    queue.append((i,j))
        while queue:
            num = len(queue)
            for i in range(num):
                cur_i,cur_j = queue.popleft()
                bfs(grid, cur_i, cur_j)
            res+=1
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    return -1
        return max(res-1,0)


if __name__ == "__main__":
    # grid = [[2,1,1],[1,1,0],[0,1,1]]
    # grid = [[0,2]]
    # grid = [[2,1,1],[0,1,1],[1,0,1]]
    grid = [[0]]
    print(Solution.orangesRotting(Solution,grid))

"""
dfs的深度不就是分钟数嘛，结束后能扫出1那就是-1，扫不出那就是深度
如果一个部分有两个坏橘子，第一次dfs将会是整个的，实际上应该是两个在起作用
通过队列把每轮要腐烂橘子扫出来，如果队列没有新加入的节点，就是结束
"""