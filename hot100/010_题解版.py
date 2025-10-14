from collections import defaultdict


class Solution:
    def subarraySum(self, nums: list[int], k: int) -> int:
        cnt = defaultdict(int)
        cnt[0] = 1
        ans = 0
        s = 0
        for x in nums:
            s+=x
            ans+=cnt[s-k]
            cnt[s]+=1
        return ans


nums =[-1,-1,1]
k=0
print(Solution.subarraySum(Solution,nums,k))

