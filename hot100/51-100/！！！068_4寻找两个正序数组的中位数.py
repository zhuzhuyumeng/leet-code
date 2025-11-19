from operator import index
from typing import List
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        size1 = len(nums1)
        size2 = len(nums2)
        index1 = 0
        index2 = 0
        sum = size1+size2-2
        mid = int(sum/2)
        while (index1+index2<=mid-1):
            if nums1[index1]<nums2[index2]:
                index1 += 1
            else:
                index2 += 1
        if sum%2==0:
            return (nums1[index1]+nums2[index2])/2
        else:
            return nums1[index1] if nums1[index1] <= nums2[index2] else nums2[index2]

# 下标就是个数，直接落到个数组的中间，然后数字大的向左，数字小的向右

if __name__ == "__main__":
    nums1 = [1,3]
    nums2 = [2]
    sol = Solution()
    print(sol.findMedianSortedArrays(nums1,nums2))