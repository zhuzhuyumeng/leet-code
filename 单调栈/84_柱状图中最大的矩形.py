from typing import List
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        size = len(heights)
        max_area = 0
        for i in range(size):
            h = heights[i]
            left = i
            while left-1 >= 0 and heights[left-1]>=h:
                left = left - 1
            right = i
            while right+1 < size and heights[right+1]>=h:
                right = right + 1
            max_area = max(max_area,h*(right-left+1)) # 边界记得+1
        return max_area


# 暴力解法，向两边扩散怎么写，两边如何动态求和，不用考虑高度比当前短的，因为会在短的高度考虑
if __name__ == "__main__":
    heights = [2, 1, 5, 6, 2, 3]
    sol = Solution()
    print(sol.largestRectangleArea(heights))
