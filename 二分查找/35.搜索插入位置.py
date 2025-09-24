class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        left = 0
        right = len(nums)-1
        while left <= right:
            mid = left + (right - left)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
        if nums[mid] > target:# 比目标大，目标取代该位置
            return mid
        elif nums[mid] < target: # 此时这个是比目标小，目标在当前的右边
            return mid+1

# 如何把最后的mid确定，因为会左右摇摆
nums = [1,3,5,6]
print(Solution.searchInsert(Solution,nums,2))