class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        leftIdx = Solution.binarySearch(self,nums ,target ,True)
        rightIdx = Solution.binarySearch(self,nums ,target ,False)-1
        if (leftIdx<=rightIdx and nums[leftIdx] == target and nums[rightIdx] == target):
            return [leftIdx,rightIdx]
        else:
            return [-1,-1]


    def binarySearch(self,nums: list[int], target: int, lower: bool) -> int:
        left = 0
        right = len(nums)-1
        ans = len(nums)
        while (left <= right):
            mid = (left + right)//2
            if (nums[mid] > target or (lower and nums[mid] >= target)):
                # 当前的大于目标值or(求较小值and当前位置涵盖=号)，lower是找较低的，right右移，返回结果ans也右移,该语句中关键部分是lower的bool值
                # 可=才会有左移，不带=只找第一个大的当找到=的时候就不符合
                right = mid - 1 # 右指针向左移动，把mid靠到最左边
                ans = mid
            else:
                left = mid + 1 # 向右移动，那就是左边的
        return ans

# 二分查找左边界，第一个大于等于target的下标
# 二分查找右边界，第一个大于target的下标-1

# nums = [3,3,3]
# nums = [1,1]
nums = [5,6,7,8,8,10]
print(Solution.searchRange(Solution, nums, 8))