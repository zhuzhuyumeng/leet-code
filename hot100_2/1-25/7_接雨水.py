class Solution:
    def trap(self,height:list[int]) -> int:
        l_list = []
        r_list = []
        n = len(height)
        l_max = 0
        r_max = 0
        for i in range(n):
            l_max= max(l_max,height[i])
            l_list.append(l_max)
        for j in range(n-1,-1,-1):
            r_max = max(r_max, height[j])
            r_list.append(r_max)
        r_list.reverse()
        sum = 0
        for i in range(n):
            sum += min(l_list[i],r_list[i])-height[i]

        return sum
    def trapdp(self,height:list[int]) -> int:
        n = len(height)
        left = 0
        right = n-1
        leftMax = 0
        rightMax = 0
        ans = 0
        while left<right:
            leftMax = max(leftMax,height[left])
            rightMax = max(rightMax,height[right])
            if height[left]<height[right]:
                ans += leftMax-height[left]
                left += 1
            else:
                ans += rightMax - height[right]
                right -= 1
        return ans
"""
动态规划：
两个数组，各取某边的最大值，两边找最小值-当前高度就是当前位置盛水的高度

单调栈：

双指针无法确定右边界啊：
双指针，为什么两个指针没有相遇的时候就可以统计接雨水的水量？
left

right

"""

if __name__ == "__main__":
    height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    print(Solution.trap(Solution,height))