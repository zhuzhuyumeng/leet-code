class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        hasmap = {}
        for i in nums:
            hasmap[i] = 0
        maxnum=0
        for j in hasmap:
            if j-1 in hasmap:
                continue
            count = 1
            while j+count in hasmap:
                count+=1
            hasmap[j] = count
            maxnum = max(maxnum,count)
        return maxnum


words = [100,4,200,1,3,2]
print(Solution.longestConsecutive(Solution, words))
# 每次从一段开头向后遍历