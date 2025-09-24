class Solution:
    # def mySqrt(selfself, x: int) -> int:
    #     left,right = 0, x
    #     while left<=right:
    #         mid = left + (right - left)//2
    #         if (mid*mid <= x) and ((mid+1)*(mid+1)>x):# 注意右这里面是否有=号
    #             return mid
    #         elif mid*mid < x:
    #             left = mid + 1
    #         elif mid*mid > x:
    #             right = mid -1
    def mySqrt(selfself, x: int) -> int:
        left, right = 0, min(x+1, 46341)
        while left + 1 < right:
            m = (left + right)//2
            if m * m <= x: # 因为是左边界，所以=号放这边
                left = m
            elif m * m > x:
                right = m
        return left

print(Solution.mySqrt(Solution,144))