from array import array


class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        left, right = 0, len(nums)-1
        array = [0 for _ in range(len(nums))]
        i = right
        while left<=right:
            if abs(nums[left]) > abs(nums[right]):
                array[i] = nums[left]*nums[left]
                left += 1
            elif abs(nums[left]) < abs(nums[right]):
                array[i] = nums[right]*nums[right]
                right -= 1
            else:
                array[i] = nums[left]*nums[left]
                left += 1
            i -= 1
        return array

nums = [-4,-1,0,3,10]
print(Solution.sortedSquares(Solution,nums))



