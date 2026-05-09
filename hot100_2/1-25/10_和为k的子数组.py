class Solution:
    def subarraySum(self,nums:list[int],k:int) -> int:
        ans = 0
        pre_num = {}
        pre_num[0] = 1 #初始为0方便计算
        # 当前和-目标值=之前的前缀和
        count = 0
        for num in nums:
            ans += num
            if ans-k in pre_num:
                count += pre_num[ans-k]
            pre_num[ans] = pre_num.get(ans,0)+1

        # 前缀和有了然后呢，前缀和是动态的不可以在统计后再进行计算
        return count
"""
数组是没有排序的，排序是不能变的
不能暴力硬扫吧
"""
if __name__ == "__main__":
    nums = [1,1,1]
    k = 2
    print(Solution.subarraySum(Solution,nums,k))