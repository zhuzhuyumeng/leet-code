from typing import List
class Solution:
    def jump(self, nums: List[int]) -> int:
        max_step = 0
        start = 0
        end = 0
        farthest = 0
        while end<len(nums)-1:
            for i in range(start,end+1):
                farthest = max(farthest,nums[i]+i)
            start = end +1
            end = farthest
            max_step += 1
        return max_step
# 这是一个区间的便民化，第一步从第一个数字开始，区间内的数字所能走的最长距离，就是下个区间的尾部





if __name__ == "__main__":
    # nums = [2,3,1,1,4]
    nums = [2,3,0,1,4]
    sol = Solution()
    print(sol.jump(nums))