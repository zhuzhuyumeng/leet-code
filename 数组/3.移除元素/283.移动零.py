class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        low, fast = 0, 0
        length = len(nums)
        while fast < length :
            if nums[fast] != 0:
                temp = nums[fast]
                nums[fast] = nums[low]
                nums[low] = temp
                low += 1
                fast += 1
            else:
                fast += 1
        return
# 当我low遇到0，就往fast交换，交换必为fast，low不是0就继续向后走
# nums = [0,1,0,3,12]
# nums = [2,1] # low指针多走
# 折磨人，自己的思路有问题呢
nums = [4,2,4,0,0,3,0,5,1,0]
# val = 0
Solution.moveZeroes(Solution, nums)
for i in range(0,len(nums)):
    print(nums[i])