from typing import List
class Solution:
    def search(self, nums: List[int], target: int) -> List[int]:
        size = len(nums)
        left = 0
        right = size-1
        while (left<=right):
            mid = int((left+right)/2)
            if nums[mid] == target:
                return mid
            if nums[left]<=nums[mid]: # 左边有序
                if target>=nums[left] and target<nums[mid]: # 左边倒反天罡
                    right = mid - 1
                else:
                    left = mid + 1
            else: #左边无序，即右边有序
                if target<=nums[right] and target>nums[mid]:
                    left = mid + 1
                else:
                    right = mid -1
        return -1
# 好思路，原本是递增的，不管怎么变，如果非顺序，左边都会大于右边

if __name__ == "__main__":
    matrix = [4,5,6,7,0,1,2]
    target = 0
    sol = Solution()
    print(sol.search(matrix,target))