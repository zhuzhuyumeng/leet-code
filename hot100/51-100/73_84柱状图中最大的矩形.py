from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        heights.append(0)# 添加0使得全部弹出
        size = len(heights)
        stack = [-1]
        max_area = 0

        for i in range(size):
            while stack[-1]!=-1 and heights[i]<heights[stack[-1]]: # 当前数字比栈顶元素小
                cur = stack.pop()# 栈顶元素下标
                left = stack[-1]
                w = i - left - 1 # 左边的栈顶就是左边界
                h = heights[cur]
                max_area = max(max_area,w*h)
            stack.append(i)
        # 此时已经走到头了

        return max_area
        # size = len(heights)
        # stack = [-1]
        # max_area = 0
        #
        # for i in range(size):
        #     while stack[-1]!=-1 and heights[i]<heights[stack[-1]]: # 当前数字比栈顶元素小
        #         cur = stack.pop()# 栈顶元素下标
        #         left = stack[-1]
        #         w = i - left - 1 # 左边的栈顶就是左边界
        #         h = heights[cur]
        #         max_area = max(max_area,w*h)
        #     stack.append(i)
        # # 此时已经走到头了
        # while stack[-1]!=-1:
        #     cur = stack.pop()
        #     left = stack[-1]
        #     width = size - left -1
        #     max_area = max(max_area,width*heights[cur])
        # return max_area


# 1.栈内元素的顺序如何确定 2同高如何处理 4栈内保存什么？
# 栈中剩下的那个就是他的左边界
        # size = len(heights)
        # max_area = 0
        # for i in range(size):
        #     h = heights[i]
        #     left = i
        #     while left-1 >= 0 and heights[left-1]>=h:
        #         left = left - 1
        #     right = i
        #     while right+1 < size and heights[right+1]>=h:
        #         right = right + 1
        #     max_area = max(max_area,h*(right-left+1)) # 边界记得+1
        # return max_area


# 暴力解法，向两边扩散怎么写，两边如何动态求和，不用考虑高度比当前短的，因为会在短的高度考虑
if __name__ == "__main__":
    # heights = [2, 1, 5, 6, 2, 3]
    heights = [2, 4,3,5]
    sol = Solution()
    print(sol.largestRectangleArea(heights))
