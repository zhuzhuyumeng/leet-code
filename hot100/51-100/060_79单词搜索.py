class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        def backtracking(visited: list[list[bool]],word:str,i:int,j:int) -> bool:
            if not word:
                return True
            if visited[i][j] == True or board[i][j]!=word[0]: # 当前被遍历过，返回重走
                return False
            if board[i][j] == word[0]:# 当前字符符合word
                if len(word) == 1:
                    return True
                visited[i][j] = True
                direction = [(1,0),(0,1),(-1,0),(0,-1)] #下，右，上，左
                for di,dj in direction:
                    ni,nj = i+di,j+dj
                    if 0<=ni<y and 0<=nj<x:
                        print("-----------")
                        print("direction="+str(di)+"|"+str(dj)+"|||"+"board[ni][nj]="+board[ni][nj])
                        if backtracking(visited,word[1:],ni,nj): # 应当在e点向左边走0,-1，但是走到上面的c是走过的，return回来，此时word退回去了
                            return True
                visited[i][j] = False
            return False

        x = len(board[0])
        y = len(board)
        visited = [[False for _ in range(x)] for _ in range(y)]
        for i in range(y):
            for j in range(x):
                if backtracking(visited, word, i, j):
                    return True
        return False


"""已经到了获得True的结果，但是结果返回不回去。还是没弄清楚
「找到就一路 return True 冲回顶层」
"""


if __name__ == '__main__':
    # board = [['A', 'B', 'C', 'E'], ['S', 'F', 'C', 'S'], ['A', 'D', 'E', 'E']]
    # word = "ABCCED"
    board = [['A', 'B', 'C', 'E'], ['S', 'F', 'C', 'S'], ['A', 'D', 'E', 'E']]
    word = "ABCB"
    solution = Solution()
    res = solution.exist(board,word)
    print(res)