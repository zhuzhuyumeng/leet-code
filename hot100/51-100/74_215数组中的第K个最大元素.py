import random
from typing import List
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        def quick_select(nums:List[int],k:int):
            pivot = random.choice(nums)
            small , base , big = [],[],[]
            for i in range(len(nums)): # 遍历放到对应位置
                if nums[i]<pivot:
                    small.append(nums[i])
                elif nums[i]==pivot:
                    base.append(nums[i])
                else:
                    big.append(nums[i])
            if len(big)>=k: #目标在big里面
                return quick_select(big,k)
            if len(nums)-len(small)<k: #k的位置在small之中，base和big还不够k个
                # len(num)-len(small)=len(base)+len(big)
                return quick_select(small,k-len(nums)+len(small)) # 去掉淘汰的大数，以及当前base
            return pivot

        res = quick_select(nums,k)
        return res

        # def quicksort(start:int,end:int):
        #     if start<end:
        #         base = nums[start]
        #         left = start
        #         right = end
        #         while left<right:
        #             while left<right and nums[right]>=base:
        #                 right -= 1
        #             nums[left] = nums[right]
        #             while left<right and nums[left]<=base:
        #                 left += 1
        #             nums[right] = nums[left]
        #         nums[left] = base
        #         if left == size-k:
        #             return nums[size-k]
        #         quicksort(start,left-1)
        #         quicksort(left+1,end)
        #
        # size = len(nums)
        # quicksort(0,size-1)
        # print(nums)
        # return nums[size-k]
# 快排并非二分，取第一个值，然后开始左右比较，直到比完，第一个数再放进那个位置

if __name__ == "__main__":
    nums = [3,2,1,5,6,4]
    k = 2
    sol = Solution()
    print(sol.findKthLargest(nums,k))