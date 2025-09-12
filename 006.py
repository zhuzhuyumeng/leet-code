class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        n = len(nums)
        list = []
        for i in range(0,n-1):
            if i>0 and nums[i]==nums[i-1]:
                continue
            l = i+1
            r = n-1
            target = -nums[i]
            while l < r:
                sum = nums[l]+nums[r]
                if sum==target:
                    list.append([nums[i],nums[l],nums[r]])
                    l+=1
                    r-=1# 在此处如果同时移动，就会有数字不变的可能，从而列表出现重复，移动应该在一块
                    while l < r and nums[r] == nums[r + 1]:
                        r -= 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                else:
                    if sum>target:
                        r -= 1
                    else:
                        l += 1
        return list

# 两数逼近应该是与目标值比，而不是两数相比
# 移动的判断尽量在一起



# nums= [-1, 0, 1, 2, -1, -4]
nums = [2,-3,0,-2,-5,-5,-4,1,2,-2,2,0,2,-4,5,5,-10]
print(Solution.threeSum(Solution,nums))