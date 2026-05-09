class Solution:
    def threeSum(self,nums:list[int]) -> list[list[int]]:
        nums.sort()
        n = len(nums)
        ans = list()

        # 重复数字利用 =去重
        for first in range(n): # 枚举第一个数字，且去重复
            if first>0 and nums[first]==nums[first-1]:
                continue
            third = n-1
            target = -nums[first]
            for second in range(first+1,n): # 枚举第二个数字，且去重复，肯定与前一个数字不一致，第二个数字的第一个与第一个数字可以是一致的
                if second>first+1 and nums[second]==nums[second-1]:
                    continue
                while second<third and nums[second]+nums[third]>target:# 和比较大，第三个数一致缩小，直至符合条件
                    third -=1
                if second==third: #不可以在此处加入 和<target就break，因为second还可以后移
                    break # 这个第二个数字与第三个数字和过大了
                if nums[second]+nums[third]==target:
                    ans.append([nums[first],nums[second],nums[third]])

        return ans

"""
三个数字位置不同，三个和为0，我只能想到暴力硬扫啊
把第一个数字当做目标值，
枚举第二个数字，第三个数字默认为最后的数字
第二三数字找符合target的值
-4 -1 -1 0 1 2
"""
if __name__ == "__main__":
    nums = [-1,0,1,2,-1,-4]
    nums = [-100,-70,-60,110,120,130,160]
    print(Solution.threeSum(Solution,nums))