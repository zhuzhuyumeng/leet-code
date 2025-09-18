class Solution:
    def rotate(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        y_len = len(matrix)
        x_len = len(matrix[0])
        ans = []
        for y in range(y_len):
            for x in range(x_len):
                ans.append(matrix[y][x])
        index = 0
        for x in range(x_len-1,-1,-1):
            for y in range(y_len):
                matrix[y][x]=ans[index]
                index+=1
        print(matrix)


# matrix = [[1,2,3],[4,5,6],[7,8,9]]
matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
print(Solution.rotate(Solution,matrix))