class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        arrary = [0 for _ in range(len(nums))]
        i = 0
        for num in nums:
            arrary[i] = num*num
            i += 1
        arrary.sort()
        return arrary


nums = [-4,-1,0,3,10]
print(Solution.sortedSquares(Solution,nums))



