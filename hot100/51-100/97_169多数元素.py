from typing import List
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dict = {}
        n = len(nums)
        total = n/2
        for i,num in enumerate(nums):
            dict[num] = dict.get(num,0)+1
        for num,value in dict.items():
            if value>total:
                return num

    def majorityElement2(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        return nums[n//2]


if __name__ == "__main__":
    nums = [3,2,3]
    nums = [2, 2, 1, 1, 1, 2, 2]
    # print(Solution.majorityElement(Solution,nums))
    print(Solution.majorityElement2(Solution, nums))