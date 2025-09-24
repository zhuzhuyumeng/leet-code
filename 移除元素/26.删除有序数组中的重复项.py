class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        fast, slow = 0, 1
        for fast in range(1,len(nums)): # 0会多判断一次，无意义
            if nums[fast] != nums[slow-1]:
                nums[slow] = nums[fast]
                slow += 1
        return slow

# nums = [0,0,1,1,1,2,2,3,3,4]
nums = [1, 3, 2]
# nums = [1]
print(Solution.removeDuplicates(Solution,nums))