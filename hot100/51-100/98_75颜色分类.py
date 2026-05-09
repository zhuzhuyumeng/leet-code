from typing import List
class Solution:
    def sortColors(self,nums:List[int]) ->None:
        left=0
        for right,num in enumerate(nums):
            if nums[right]==0:
                tmp = nums[left]
                nums[left] = nums[right]
                nums[right] = tmp
                left +=1
        for right in range(left,len(nums)):
            if nums[right] == 1:
                tmp = nums[left]
                nums[left] = nums[right]
                nums[right] = tmp
                left += 1
        return nums

    def sortColors2(self, nums: List[int]) -> None:
        p0 = 0
        p1 = 0
        # p0,p1都是待验证的位置，
        for i in range(len(nums)):
            if nums[i]==0:
                nums[p0], nums[i] = nums[i], nums[p0]
                if p0 < p1:
                    # 可能把第一个1交换出去
                    nums[p0],nums[p1] = nums[p1],nums[p0]
                p0 +=1
                p1 +=1
            if nums[i]==1:
                # 1这个数字是在中间位置的
                nums[p1], nums[i] = nums[i], nums[p1]
                p1 += 1
        return nums
"""
原地排序，双指针？
0  1  2  3  4  5

2  0  2  1  1  0
p0,p1=0,0
0  2  2  1  1  0
p0,p1=1,1
0  1  2  2  1  0
p0,p1=1,2
0  1  1  2  2  0
p0,p1=1,3
0  0  1  2  2  1
0  0  1  1  2  2
p0,p1=2,4
p0和i交换，但是此时p0<p1，所以还有i与p1的互换
"""
if __name__ == "__main__":
    nums = [2, 0, 2, 1, 1, 0]
    print(Solution.sortColors(Solution,nums))