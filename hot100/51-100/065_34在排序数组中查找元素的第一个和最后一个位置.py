from typing import List
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        size = len(nums)
        left = 0
        right = size-1
        ans = size
        while (left<=right):
            mid = int((left+right)/2)
            if target<=nums[mid]:
                ans = mid
                right = mid - 1
            else:
                left = mid + 1
        if ans == size or nums[ans]!=target:
            return [-1,-1]
        left = right = ans
        while left-1>0 and nums[left - 1] == target:
            left -= 1
        while right+1<size and nums[right+1] == target:
            right += 1
        return [left,right]

if __name__ == "__main__":
    matrix = [5,7,7,8,8,10]
    target = 8
    sol = Solution()
    print(sol.searchRange(matrix,target))