class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        fast, slow = 0, 0
        ans = len(nums)
        for fast in range(0,ans):
            if ( nums[fast] != val ):
                nums[slow] = nums[fast]
                slow += 1
        return slow

nums = [3,2,2,3]
val = 3
print(Solution.removeElement(Solution, nums, val))
