class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def reverse(i:int,j:int):
            while i<j:
                nums[i],nums[j]=nums[j],nums[i]
                i+=1
                j-=1
        n=len(nums)
        k = k%n
        reverse(0,n-1)
        reverse(0,k-1) # 0,1,2
        reverse(k,n-1)
        print(nums)


nums = [1,2,3,4,5,6,7]
k = 3
print(Solution.rotate(Solution,nums,k))

"""
cnt = []
n = len(nums)
index = 0
for i in range(n-k,n):
    cnt.append(nums[i])
for i in range(0,n-k):
    cnt.append(nums[i])
nums = cnt
print(nums)
"""