from collections import defaultdict


class Solution:
    def subarraySum(self, nums: list[int], k: int) -> int:
        cnt = defaultdict(int)
        cnt[0] = 1
        ans=0
        s = 0
        for x in nums:
            s+=x # 前缀和
            ans+=cnt[x-k] # 前缀和差
            cnt[s]+=1 # 前缀和加上去
        return ans


nums =[-1,-1,1]
k=0
print(Solution.subarraySum(Solution,nums,k))

