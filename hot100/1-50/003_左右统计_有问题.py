class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        hashmap = {}
        n = len(nums)
        for i in range(n):
            left = i
            left_len = 0
            right = i
            right_len = 0
            flag = 1
            hashmap[nums[i]] = 0
            while nums[i]-flag in hashmap: # 如果这个左边的数字存在
                left_len+=1
                flag+=1
            flag=1
            while nums[i]+flag in hashmap: # 如果这个左边的数字存在
                right_len+=1
                flag+=1
            hashmap[nums[i]] = left_len+right_len+1
        max_num = 0
        # [100,4,200,1,3,2],在2的时候右边长度并没有到2，因为flag没有复位
        for i in hashmap:
            max_num = max(hashmap[i],max_num)
        return max_num
            # 该数字位置的统计值，那如何统计呢，如果
            # 放一个数字进去，前面没有，就是1。1，3，后面加入了2，如何更新？
            # 每个数字存储左边长度和右边长度。对数字求和找最大。
            # 所以怎么求左右长度，key取值顺序比较是否差1吗？
            # 第一步，把这个数字放进去
            # 第二步，检查左右长度，和value为左+右+1
            # 每次维护太大了，测试样例十万，每个都要测一遍。
            # 我维护一个左右的，
            # 第三步，遍历字典取最大value

words = [2,2,2,2]
print(Solution.longestConsecutive(Solution, words))

# 第一思路是数组排序，然后对排序后的数组比大小，但是本题给的是哈希
# 让这些数字实体上相邻，选取最大的连续实体。如何表示这种实体，key和value分别表示什么？
# 如果key表示的是这个数字，value存的是这个数字之前的相邻的数字，包括这个数字的个数
