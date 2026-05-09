class Solution:
    def searchMatrix(self, matrix: list[list[int]]) -> list[int]:
        m = len(matrix[0])
        n = len(matrix)
        x=m-1
        y = 0
        while(y<n and x>0):
            print(f"[x,y][{x,y}]")
            if matrix[y][x] == target:
                return True
            if matrix[y][x] < target:
                y+=1
            else:
                x -= 1
        return False


"""
z字形查找
如何对x，y进行移动的呢？
初始化是右对角线的起点，只要比一边就可以了，否则要比较两边
行元素从左到右升序
[[1,4,7,11,15],
[2,5,8,12,19],
[3,6,9,16,22],
[10,13,14,17,24],
[18,21,23,26,30]]
列元素从上到下升序
"""
if __name__ == "__main__":
    matrix = [[1, 4, 7, 11, 15], [2, 5, 8, 12, 19], [3, 6, 9, 16, 22], [10, 13, 14, 17, 24], [18, 21, 23, 26, 30]]
    target = 20
    print(Solution.searchMatrix(Solution,matrix))