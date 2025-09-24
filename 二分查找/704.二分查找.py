nums = [-1,0,3,5,9,12]
class Solution:
    def search(self, nums: list[int], target: int) -> int:
        n = len(nums)
        left = 0
        right = n-1
        # while left<=right:
        #     mid = (left + right)//2
        #     if nums[mid] == target:
        #         return mid
        #     elif nums[mid] < target:
        #         left = mid+1
        #     elif nums[mid] > target:
        #         right = mid-1
        while left<right:
            mid = (left + right)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
        return -1

# 小数如何处理
# 左闭右闭，左闭右开，指left和right
# i+j超出上限？i+(j-i)/2
# left + ((right - left) // 2)
print(Solution.search(Solution,nums,9))