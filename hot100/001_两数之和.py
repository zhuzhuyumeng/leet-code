class Solution:
    def twoSum(self,nums: list[int], target: int) -> list[int]:
        # n = len(nums)
        # for i in range(n):
        #     for j in range(i+1,n):
        #         if nums[i]+nums[j]==target:
        #             return [i,j]
        # return []
        hashmap = {}
        for i,num in enumerate(nums):
            if target - num in hashmap:
                return [hashmap[target - num],i]
            hashmap[nums[i]]=i
        return []

nums = [2,7,11,15]
# nums = [3,2,4]
target = 9
print(Solution.twoSum(Solution,nums, target))
# 两数之和，不能使用两次相同的元素
"""
对数组排序？不太合理吧
遍历？两个for循环是可以做到的，但是有没有其他方法呢？
hash表？怎么做到。字典。一个数字放进去，怎么存储位置。字典[]取值，for循环用range
i是位置，num是值。hashmap记录了位置为值与数字为键
"""