class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        n=len(nums)
        presum=[1]*n
        sufsum=[1]*n
        for i in range(1,n):
            presum[i]=presum[i-1]*nums[i-1]
        for i in range(n-2,-1,-1):
            sufsum[i]=sufsum[i+1]*nums[i+1]
        result = []
        for i in range(0,n):
            result.append(presum[i]*sufsum[i])
        return result

nums = [1,2,3,4]
# [1,1,2,6]
# [24,12,4,1]
print(Solution.productExceptSelf(Solution,nums))
# 前缀和后缀都统计