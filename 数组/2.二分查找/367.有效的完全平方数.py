class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        left, right = 0, num
        if num == 1:
            return True
        while left + 1 < right: # 神奇的+1
            m = left + (right - left)//2
            if m * m == num:
                return True
            elif m * m < num:
                left = m
            elif m * m > num:
                right = m
        return False

    # 二分查找
    def isPerfectSquare2(self, num: int) -> bool:
        left, right = 0, num
        while left <= right:  # 这个=号配上左右移动
            m = left + (right - left) // 2
            square = m * m
            if m * m < num:
                left = m + 1
            elif m * m > num:
                right = m - 1
            else:
                return True
        return False

print(Solution.isPerfectSquare2(Solution,1))
