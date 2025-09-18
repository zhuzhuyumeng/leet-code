class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        left = 0
        right = 0
        while right<n:# 中间那个数你就不管他
            if nums[right]!=0:
                k = nums[right]
                nums[right] = nums[left]
                nums[left] = k
                left+=1
                right+=1
            else:
                right+=1
        print(nums)
        return
# 还需要保持顺序
# 自己换自己也是可以的，然后非零向后移动

nums = [1,232,0,3,0]
Solution.moveZeroes(Solution,nums)
