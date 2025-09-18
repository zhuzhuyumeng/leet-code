class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        new = nums.sort() # 排序完就不会重复了
        n = len(nums)
        list = []
        for i in range(0,n):#从第一层开始进行twoSum，target为i
            if (i>0 and nums[i]==nums[i-1]):#这样不是把第二个-1跳过了吗，去重有点过了
                continue
            l = i+1
            r = n-1
            while (l<r):
                if nums[l]+nums[r]==-nums[i]:
                    list.append([nums[i],nums[l],nums[r]])
                    l+=1
                    r-=1
                    continue
                if abs(nums[l])>abs(nums[r]):
                    l+=1
                    while (nums[l] == nums[l-1] and l<r):
                        l+=1
                else:
                    r-=1
                    while (nums[r] == nums[r+1] and l<r):
                        r-=1
        return list
        # 位置不相同就可以了，移动是否可以做成大小？
        # 整数数字的位置各不相同，三元组还不能重复，如何对多次重复的进行排除，
        # 那就是移动一直到新数字，左右如何选择，
        # 应该在列表加新的之后就开始移动，如何一次
        # 重复的数组怎么处理啊

# 这个双指针也不好缩小范围啊
nums = [-1,0,1,2,-1,-4] #[-4,-1,-1,0,1,2]
# nums=[0,0,0,0]
# [-1,-1,0,1]
print(Solution.threeSum(Solution,nums))

# while left < right:
#     for j in range(left + 1, right):
#         if nums[left] + nums[j] + nums[right] == 0:
#             list.append([nums[left], nums[j], nums[right]])
#             break
#     if abs(abs(nums[left]) > abs(nums[right])):
#         while abs(abs(nums[left]) > abs(nums[right])):
#             left += 1
#             if (nums[left] != nums[left - 1]) or right <= left:
#                 break
#     else:
#         while abs(abs(nums[left]) <= abs(nums[right])):
#             right -= 1
#             if (nums[right] != nums[right + 1]) or right <= left:
#                 break