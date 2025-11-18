from typing import List
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        y = len(matrix)
        x = len(matrix[0])
        low = 0
        height = y-1
        y_ans = y
        while (low<=height): #扫y轴，
            mid = int((low+height)/2)
            if (target<=matrix[mid][0]): # 如果目标值小于当前值，高的往下走
                y_ans = mid
                height = mid - 1
                if target==matrix[mid][0]:
                    return True
            else:
                low = mid+1
        if y_ans == y:#超过了就要回到最后一行
            y_ans-=1
        elif target<matrix[y_ans][0]:#目标比现在第一个的小，退一行
            y_ans -= 1

        left = 0
        right = x - 1
        x_ans = x
        while (left<=right): # 扫x轴
            mid = int((left+right)/2)
            if (target<=matrix[y_ans][mid]):
                x_ans = mid
                right = mid - 1
            else:
                left = mid+1
        if x_ans == x: # 落在最后就超出了
            return False
        if matrix[y_ans][x_ans]==target: # 符合
            return True
        else:
            return False

if __name__ == "__main__":
    # matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
    matrix = [[1]]
    target = 2

    sol = Solution()
    print(sol.searchMatrix(matrix,target))