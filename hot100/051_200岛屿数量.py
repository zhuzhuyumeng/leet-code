class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        def initialvisited(grid: list[list[str]]) -> list[list[str]]:
            visited = [['0' for _ in range(x)] for _ in range(y)]
            return visited

        def dfs(i: int, j: int):
            directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
            visited[i][j] = '1'
            for di, dj in directions:
                ni, nj = i + di, j + dj
                if 0 <= ni < y and 0 <= nj < x and grid[ni][nj] == '1' and visited[ni][nj] == '0':
                    dfs(ni, nj)

        def land(grid: list[list[str]], visited: list[list[str]]) -> int:
            count = 0
            for i in range(y):
                for j in range(x):
                    if grid[i][j] == '1' and visited[i][j] == '0':  # 没走到过的陆地，全向尝试
                        dfs(i, j)
                        count += 1
                    if grid[i][j] == '0':# 走到水面，我走过了
                        visited[i][j] = '1'
                    else:
                        # visited[i][j] = '1'# 微微提高了时间
                        continue #你咋对时间还有影响
            return count

        y = len(grid)
        if y:
            x = len(grid[0])
        else:
            x = 0
        visited = initialvisited(grid)
        count = land(grid, visited)
        print(visited)
        return count



# grid = [
#   ['1','1','1','1','0'],
#   ['1','1','0','1','0'],
#   ['1','1','0','0','0'],
#   ['0','0','0','0','0']
# ]
grid = [
  ['1','1','0','0','0'],
  ['1','1','0','0','0'],
  ['0','0','1','0','0'],
  ['0','0','0','1','1']
]
print(Solution.numIslands(Solution,grid))

"""
1陆地，0水
陆地在水平竖直方向可相连
"""