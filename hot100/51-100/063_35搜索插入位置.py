from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        size = len(nums)
        if size<1:
            return 0
        left = 0
        right = size-1
        mid = int((left + right) / 2)
        ans = size
        while left<=right:
            mid = int((left+right)/2)
            if (target<=nums[mid]):
                ans = mid
                right = mid - 1
            else:
                left = mid +1
        return ans


if __name__ == "__main__":
    nums = [1,3,4,6]
    target = 7
    # nums = [1,3]
    # target = 2
    sol = Solution()
    print(sol.searchInsert(nums,target))
