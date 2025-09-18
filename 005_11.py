class Solution:
    def maxArea(self, height: list[int]) -> int:
        n = len(height)
        left = 0
        right = n-1
        max_sum = 0
        while left<right:
            max_sum = max((right-left)*min(height[left],height[right]),max_sum)
            # 宽度*两边最低高度
            if height[left]<height[right]:
                left+=1
            else:
                right-=1
        return max_sum


# 接最多雨水？
# 每次都要看前面最高的？我觉得可以,
# 不可以这样，如果是一个扁平化的就错啦
# 如果是双指针，指针如何变化，刚开始都在左右两边。那就一点点缩进？但是不能两边都缩进啊。
# 移动数值较小的，因为大的有机会更大
height = [1,8,6,2,5,4,8,3,7]
print(Solution.maxArea(Solution,height))