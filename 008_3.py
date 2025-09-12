class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        hash_map = dict()
        left = 0
        max_num = 0
        # for i in range(n):
        #     if s[i] in hash_map:
        #         # 移动 left 到重复字符的下一个位置
        #         left = max(left, hash_map[s[i]] + 1)
        #     # 无论是否重复，都要更新字符的最新位置
        #     hash_map[s[i]] = i
        #     max_num = max(max_num, i - left + 1)
        # return max_num
        for i in range(n):
            if s[i] in hash_map:# 如果出现了这个字符，左指针立刻移动到出现该字符的右边，
                # 前面移动的字符会出现未清空的现象，所以就需要比较快慢，
                # 如果未清空的再次出现，要与当前left比较，右指针照常添加就可以了
                left = max(hash_map[s[i]]+1,left) # 重复值的位置再向右移动
            hash_map[s[i]]=i
            max_num = max(max_num,i-left+1)
        return max_num
# 双指针可以吗，慢慢滑动呗
# s = "abcabcbb"
# s= "bbbb"
s = "tmmzuxt"
print(Solution.lengthOfLongestSubstring(Solution,s))