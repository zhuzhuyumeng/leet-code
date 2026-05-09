from typing import List
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        n = len(nums)
        left = 0
        for right,num in enumerate(nums):
            if right==0:
                continue
            if nums[right]>nums[left]:
                # 1,2,3，非常正常嗷，直接拉到最后


"""
并非简单换一个数字，而是需要整体排序
1324
1234
4321 倒序递增直接翻转完事
"""
if __name__ == "__main__":
    nums = [1,2,3]
    print(Solution.nextPermutation(Solution,nums))