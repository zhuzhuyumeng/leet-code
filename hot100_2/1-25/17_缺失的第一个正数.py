class Solution:
    def firstMissingPostive(self, nums:list[int]) -> None:
        hashtable = {}
        n = len(nums)
        for i in range(n):
            hashtable[nums[i]] = 1
        for num in range(1,n+1):
            if num not in hashtable:
                return num
        print(hashtable)
        return n+1

"""
不包含0，一直到n
不对，负数有问题
"""
if __name__ == "__main__":
    nums = [1,2,0]
    nums = [3, 4, -1, 1]
    print(Solution.firstMissingPostive(Solution,nums))