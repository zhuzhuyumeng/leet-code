class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        left = 0
        right = len(nums) - 1
        flag = 0
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                flag = 1
                break
            elif nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
        if flag == 0:
            return [-1,-1]
        elif flag == 1:
            leftb = mid
            rightb = mid
            lflag = 1
            rflag = 1
            if mid == 0:
                lflag = 0
            if mid == len(nums)-1:
                rflag = 0
            while lflag and leftb-1>-1 and nums[leftb-1] == target:
                leftb -= 1
            while rflag and rightb+1<len(nums) and nums[rightb+1] == target:
                rightb +=1
            return [leftb,rightb]

# 左右两边都可能有啊
# 如何对这个边界进行判断，找到就开始向左右遍历寻找

nums = [3,3,3]
# nums = [1,1]
# nums = [5,6,7,8,8,10]
print(Solution.searchRange(Solution, nums, 3))