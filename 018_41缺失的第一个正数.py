from collections import defaultdict


class Solution:
    def firstMissingPositive(self, nums: list[int]) -> int:
        hashmap = defaultdict(int)
        n = len(nums)

        for i in range(0,n):
            if nums[i]<=0 and nums[i]>n+1:
                nums[i]=n+1
            hashmap[nums[i]] +=1
        index = 1
        while index <=n:
            if hashmap[index]==0:
                return index
            index+=1
        return n+1


nums = [1,2,0]
print(Solution.firstMissingPositive(Solution,nums))