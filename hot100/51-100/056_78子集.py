class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        res = [[]]
        for i in range(len(nums)):
            for j in range(len(res)):
                res.append(res[j]+[nums[i]])
        return res


if __name__ == '__main__':
    nums = [1,2,3]
    solution = Solution()
    res = solution.subsets(nums)
    print(res)