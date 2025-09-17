class Solution:
    def firstMissingPositive(self, nums: list[int]) -> int:
        n = len(nums)
        # 符合，位置不符，数字重复
        for i in range(n):
            while 1 <=nums[i] and nums[i]<=n and nums[i] !=nums[nums[i]-1]:
                j = nums[i]-1# 真实数组位置
                nums[i],nums[j]=nums[j],nums[i]
        for i in range(n):
            if nums[i]!=i+1
                return i+1
        return n+1



nums = [1,2,0]
print(Solution.firstMissingPositive(Solution,nums))