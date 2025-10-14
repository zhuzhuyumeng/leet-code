class Solution:
    def subarraySum(self, nums: list[int], k: int) -> int:
        prefix_num = dict()
        prefix_num[0]=1
        n_len = len(nums)
        sum = 0
        count = 0

        for i in range(n_len):
            sum = sum + nums[i]
            if (sum-k) in prefix_num:
                count = count+prefix_num[sum-k]
            if sum not in prefix_num:
                prefix_num[sum] = 1
            else:
                prefix_num[sum] += 1
        return count



# 直接滑动，较大就左移，较小就右移，不对，这是数组未排序
# 前缀和，获取每个位置的前缀和，统计前缀和的差值为k的个数
# 第一个没必要给0，步骤不要分开，应当在计算前缀和和对应hash表时计算，便不会有先后的问题
# 第一步加的0被计算了无数遍
# nums = [1,1,1]
# k = 2
# nums = [1]
# k = 0
nums =[-1,-1,1]
k=0
print(Solution.subarraySum(Solution,nums,k))