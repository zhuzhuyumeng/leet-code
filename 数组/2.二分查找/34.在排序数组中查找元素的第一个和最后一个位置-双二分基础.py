class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        def getRightBorder(nums: list[int], target: int) -> int:
            left, right = 0, len(nums)-1
            rightBorder = -2
            while(left <= right):
                mid = left + (right - left) // 2
                # 0 0 mid 0 0 target 0 0
                if nums[mid] <= target : # 找右边界，如何向右看齐
                    left = mid + 1
                    rightBorder = left #大于就走不到这里了，注意上下顺序

                else:
                    right = mid - 1
            return rightBorder

        def getLeftBorder(nums: list[int], target: int) -> int:
            left, right = 0, len(nums)-1
            leftBorder = -2
            while(left <= right):
                mid = left + (right - left) // 2
                # 0 0 mid 0 0 target 0 0
                if nums[mid] >= target : # 找左边界，如何向左看齐
                    right = mid - 1
                    leftBorder = right  # 大于就走不到这里了
                else:
                    left = mid + 1
            return leftBorder

        leftBorder = getLeftBorder(nums,target)
        rightBorder = getRightBorder(nums,target)
        if leftBorder == -2 or rightBorder == -2:
            return [-1,-1]
        if rightBorder - leftBorder > 1:
            # 这个判断，在判断中相关顺序各多走一步如果只出现一个，那就是多123，差2，
            return [leftBorder+1, rightBorder-1]
        return [-1,-1]



# nums = [3,3,3]
# nums = [1,1]
nums = [5,6,7,8,8,10]
print(Solution.searchRange(Solution, nums, 8))