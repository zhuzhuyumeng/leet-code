import collections

class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        mp = collections.defaultdict(list)
        # 访问一个不存在的键时，自动创建一个新的空列表作为默认值
        for str in strs:
            count = [0]*26
            for ch in str:
                count[(ord(ch)-ord('a'))]+= 1
            mp[tuple(count)].append(str) 
            print(mp)
        return list(mp.values())

words = ["eat","tea","tan","ate","nat","bat","aaaa"]
print(Solution.groupAnagrams(Solution,words))
# 字母异位词组合在一起，字母是一致的
# 我要如何加入哈希表表示这个字母出现的次数，计数的思想
# 列表转为元组，列表是不可哈希的，元组是可以的
