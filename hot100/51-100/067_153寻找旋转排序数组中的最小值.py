import sys
from typing import List
class Solution:
    def findMin(self, nums: List[int]) -> List[int]:
        size = len(nums)
        left = 0
        right = size-1
        while (left<right):
            mid = int((left+right)/2)
            if nums[mid]>nums[right]:# mid是较大的，所以可以放心跳过，往右边找
                left = mid + 1
            else:# 往左边找
                right = mid # 因为有可能mid位置就是最小值
        return nums[left]
# 如何比较出最小值，这个值的左边一定是比他大，或者根本没有

if __name__ == "__main__":
    nums = [4,5,6,7,0,1,2]
    sol = Solution()
    print(sol.findMin(nums))