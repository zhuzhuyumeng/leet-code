from typing import List
class Solution:
    def trap(self, height: List[int]) -> int:
        size = len(height)
        stack = []
        count = 0
        for i in range(size):
            while stack and height[i]>height[stack[-1]]:
                # 栈顶元素出栈
                cur = stack.pop()
                if len(stack)==0:
                    break
                # 找到较小的
                left = stack[-1]
                w = i-left-1
                min_num = min(height[i],height[left])
                h = min_num - height[cur]
                count += h * w
            stack.append(i)
        return count

# 单调栈，如果当前柱子大于栈顶元素，栈顶元素就是放水的位置，太妙了，水平接水
        # size = len(height)
        # left = []
        # right = []
        # left_max = 0
        # right_max = 0
        # for i in range(size):
        #     left_max = max(height[i],left_max)
        #     left.append(left_max)
        # for j in range(size-1,-1,-1):
        #     right_max = max(height[j], right_max)
        #     right.append(right_max)
        # right.reverse()
        # count = 0
        # for k in range(size):
        #     min_num = min(left[k],right[k])
        #     if min_num > height[k]:
        #         count += min_num - height[k]
        # return count

# 两个数组，一个保存左边最高，一个保存右边最高
# 左右两边选取较低的，减去当前的
# 向右找最高点
if __name__ == "__main__":
    # height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    height = [4, 2, 0, 3, 2, 5]
    sol = Solution()
    print(sol.trap(height))
