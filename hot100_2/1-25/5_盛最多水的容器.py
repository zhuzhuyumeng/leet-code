class Solution:
    def maxwater(self,height:list[int]) -> int:
        n = len(height)
        left = 0
        right = n-1
        maxwater = 0

        while left<right:
            kuan = right-left
            maxwater = max(maxwater, kuan * min(height[left],height[right]))
            # 还可以优化，高度比我高的才计算，因为宽度是一定在减小的
            if height[left]<height[right]:
                left += 1
            else:
                right -= 1
        return maxwater

if __name__ == "__main__":
    height = [1,8,6,2,5,4,8,3,7]
    print(Solution.maxwater(Solution,height))