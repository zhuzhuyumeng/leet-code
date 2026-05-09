from logging import fatal
from typing import List
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        fast, slow = 0, 0
        # slow走一步，fast走两步
        slow = nums[slow]
        fast = nums[nums[fast]]
        while slow!=fast:
            slow = nums[slow]
            fast = nums[nums[fast]]
        slow = 0
        while slow!=fast:
            slow = nums[slow]
            fast = nums[fast]
        return fast

    def findDuplicateFalse(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(n):
            for j in range(i):
                if nums[j] == nums[i]:
                    return nums[i]
"""
  1 4 6 6 6 2 3
  0 1 2 3 4 5 6
数字都不同，所以总是可以遍历的，重复的数字那就是一个圈哦
那为什么这个圈是slow从0开始呢
"""

if __name__ == "__main__":
    nums = [1,3,4,2,2]
    nums = [3, 1, 3, 4, 2]
    print(Solution.findDuplicate(Solution,nums))