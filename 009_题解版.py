class Solution:
    def findAnagrams(self, s: str, p: str) -> list[int]:
        s_length = len(s)
        p_length = len(p)
        llist = []
        if s_length<p_length:
            return llist

        s_count = [0]*26# 位置放对应的，值为个数
        p_count = [0]*26

        for i in range(p_length):# 给目标数据加载，顺便主也加载
            p_count[ord(p[i])-97]+=1
            s_count[ord(s[i])-97]+=1
        if s_count == p_count:# 一致就加入
            llist.append(0)
        for i in range(s_length-p_length):# 前退后补，一致就加
            s_count[ord(s[i])-97]-=1
            s_count[ord(s[i+p_length])-97] += 1
            if s_count == p_count:
                llist.append(i+1)

        return llist

s = "baa"
p = "aa"
print(Solution.findAnagrams(Solution, s, p))