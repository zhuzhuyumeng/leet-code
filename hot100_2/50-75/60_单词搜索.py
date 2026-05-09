class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        def backtracking(visited,i,j,word_index):
            if board[i][j] != word[word_index]:
                return False
            if word_index == len(word)-1:
                return True
            directions = [(1,0),(0,1),(-1,0),(0,-1)]
            visited[i][j] = True
            for dx,dy in directions:
                x = j+dx
                y = i+dy
                if 0<=x<m and 0<=y<n and visited[y][x]==False: #界内没走过
                    if backtracking(visited,y,x,word_index+1):
                        return True
            visited[i][j] = False
            return False

        m = len(board[0])
        n = len(board)
        visited = [[False for j in range(m)]for i in range(n)]
        for i in range(n):
            for j in range(m):
                word_index = 0
                if backtracking(visited, i, j, word_index):
                    return True
        return False

"""已经到了获得True的结果，但是结果返回不回去。还是没弄清楚
「找到就一路 return True 冲回顶层」
"""


if __name__ == '__main__':
    board = [['A', 'B', 'C', 'E'], ['S', 'F', 'C', 'S'], ['A', 'D', 'E', 'E']]
    word = "ABCCED"
    # board = [['A', 'B', 'C', 'E'], ['S', 'F', 'C', 'S'], ['A', 'D', 'E', 'E']]
    # word = "ABCB"
    solution = Solution()
    res = solution.exist(board,word)
    print(res)