import collections

class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:
        def infectOranges(i: int,j: int):
            directions = [(1,0),(0,1),(-1,0),(0,-1)] #四个方向，对定点的四个方向进行处理
            nxt = []
            for di,dj in directions:
                ni, nj = i+di, j+dj
                if 0<=ni<y and 0<=nj<x and grid[ni][nj] == 1:
                    grid[ni][nj] = 2
                    nxt.append((ni,nj))
            return nxt


        deque = collections.deque()
        cnt = -1
        y = len(grid)
        if y:
            x = len(grid[0])
        else:
            x = 0
        for i in range(y):
            for j in range(x):
                if grid[i][j] == 2:
                    deque.append((i,j))
        if len(deque) == 0: # 第一步就没有腐烂果子的情况
            for i in range(y):
                for j in range(x):
                    if grid[i][j] == 1:
                        return -1
            return 0
        size = len(deque)
        new_size = 0
        while size:
            loc = deque.popleft()
            i,j = loc
            for ni, nj in infectOranges(i,j):
                deque.append((ni,nj))
                new_size += 1
            size-=1
            if size == 0 :
                cnt+=1
                size = new_size
                new_size = 0

        for i in range(y):
            for j in range(x):
                if grid[i][j] == 1:
                    return -1

        return cnt

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