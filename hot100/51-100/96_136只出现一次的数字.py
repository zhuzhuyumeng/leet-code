from typing import List
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        collect = {}
        for i,num in enumerate(nums):
            collect[num] = collect.get(num,0)+1
        for num,value in collect.items():
            if value==1:
                return num
        return -1

if __name__ == "__main__":
    nums = [2,2,1]
    nums = [4, 1, 2, 1, 2]
    print(Solution.singleNumber(Solution,nums))