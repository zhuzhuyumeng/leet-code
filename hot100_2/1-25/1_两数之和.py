class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        hash = dict()
        n = len(nums)
        for i in range(n):
            if target-nums[i] in hash:# 存在这个数字
                return [hash.get(target-nums[i]),i]
            else: # 不存在就加入到哈希表中
                hash[nums[i]] = i
        return []

    def twoSum2(self,nums:list[int],target:int) -> list[int]:
        hash = dict()
        n = len(nums)
        for i in range(n):
            for j in range(i):
                count = nums[i] + nums[j]
                hash.get(count,0)+1
                if count == target:
                    return [j,i]
        return None

if __name__ == "__main__":
    # nums = [2,7,11,15]
    nums = [9,9]
    target = 18
    print(Solution.twoSum(Solution,nums,target))