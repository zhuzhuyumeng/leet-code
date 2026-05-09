import collections


class Solution:
    def groupAnagrams(self,strs:list[str]) -> list[list[str]]:
        hash = collections.defaultdict(list)# 字典里面是列表
        for str in strs:
            count = [0]*26
            for ch in str:
                count[ord(ch)-ord("a")]+=1 #字母计数
            # print(count)
            # print(tuple(count)) # 每个单词的字符统计元组，列表转元组，用来在hash表中确定位置
            hash[tuple(count)].append(str) # 在这里排序比较
        return list(hash.values())


if __name__ == "__main__":
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    print(Solution.groupAnagrams(Solution,strs))
