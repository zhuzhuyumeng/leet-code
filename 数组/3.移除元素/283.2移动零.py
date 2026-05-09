class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        slow , fast = 0,0
        n = len(nums)
        for fast in range(0,n):
            if nums[fast] !=0:
                nums[slow],nums[fast] = nums[fast],nums[slow]
                slow+=1
# slow找0，fast找0后面第一个非0，起始不好找，我希望fast不用回到slow的位置重复找

nums = [2,0,0]
# nums = [4,2,4,0,0,3,0,5,1,0]
Solution.moveZeroes(Solution, nums)
print(nums)
