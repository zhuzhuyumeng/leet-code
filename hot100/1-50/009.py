import sys
class Solution:
    def findAnagrams(self, s: str, p: str) -> list[int]:
        s_length = len(s)
        p_length = len(p)
        s_hash_map = dict()
        p_hash_map = dict()
        llist = []
        for i in range(p_length):
            p_hash_map[p[i]]=1
        # print(p_hash_map)
        for i in range(s_length):
            if s[i] in s_hash_map:
                temp = s_hash_map[s[i]]
            # 更新列表
                s_hash_map[s[i]] = i
                pop_list = []
                for key in s_hash_map:
                    if s_hash_map[key]<temp:
                        pop_list.append(key)
                for key in pop_list:
                    s_hash_map.pop(key)
            else:
                s_hash_map[s[i]] = i
            if len(s_hash_map)==len(p_hash_map):
                min_sum = sys.maxsize
                is_valid = True
                for key in s_hash_map.keys():
                    if key not in p_hash_map:
                        is_valid = False
                        break
                    min_sum = min(min_sum,s_hash_map[key])
                if is_valid == True:
                     llist.append(min_sum)
        return llist
            
# i遍历主字符串，出现一个字符放进主hash表中，
# 如果有重复的就要把他pop出去，value较小的也要出去，不对吧，又不是重复字符，如果是不符的字符也得出去啊
# 遍历副字符串，如果主副hash的key一致，就从主hash的value中选出最小值，
# 那如何判断key是否一致
# 服了，没有统计数字出现的次数
# s = "cbaebabacd"
# p = "abc"
# s = "abab"
# p = "ab"
s = "baa"
p = "aa"
print(Solution.findAnagrams(Solution, s, p))

