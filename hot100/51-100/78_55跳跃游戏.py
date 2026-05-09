from typing import List
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        max_step = 1
        for num in nums:
            max_step -= 1
            if max_step == -1:
                return False
            if num>max_step:
                max_step = num
        return True

# 每前进一步消耗一个步数，前进时需要刷新最大的步数，步数为-1就是没步数了


if __name__ == "__main__":
    # nums = [2,3,1,1,4]
    nums = [3,2,1,0,4]
    sol = Solution()
    print(sol.canJump(nums))