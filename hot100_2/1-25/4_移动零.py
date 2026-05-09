class Solution:
    def moveZeroes(self,nums:list[int]) ->None:
        n = len(nums)
        slow = 0
        for fast in range(n):
            if nums[fast] != 0:
                nums[fast],nums[slow] = nums[slow],nums[fast]
                slow += 1
        print(nums)
        return None

if __name__ == "__main__":
    nums = [0, 1, 0, 3, 12]
    print(Solution.moveZeroes(Solution,nums))