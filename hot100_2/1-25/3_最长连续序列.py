from itertools import count


class Solution:
    def findlong(self,nums:list[int]) -> int:
        hashtable = dict()
        maxnum =0
        for num in nums: #创建一个hash表存储所有已有的数字序列
            hashtable[num] = 0
        for j in hashtable:
            if j-1 in hashtable: # 对每段最小的数字，往后找出最长序列
                continue
            count = 1
            while j+count in hashtable:#一直找到最后面
                count += 1
            maxnum = max(maxnum,count)
        return maxnum
"""
{
1,   0
2,   0
3,   0
4,   0
100, 0
200, 0

}
"""
# 并非每个数字放进去的时候判断位置，而是从最小的开始算
if __name__ == "__main__":
    nums = [100, 4, 200, 1, 3, 2]
    print(Solution.findlong(Solution,nums))