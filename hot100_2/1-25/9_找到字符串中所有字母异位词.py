class Solution:
    def findAnagrams(self,s:str,p:str) -> list[int]:
        ans = []
        pdict = dict()
        sdict = dict()

        for ch in p:
            pdict[ch] = pdict.get(ch,0)+1

        left = 0
        for right,ch in enumerate(s):
            sdict[ch] = sdict.get(ch,0)+1
            while ch in pdict and sdict[ch] > pdict[ch]: # 新增的某个字符超过了原词的个数
                sdict[s[left]]-=1
                if sdict[s[left]] == 0:
                    sdict.pop(s[left])
                left += 1
            if ch not in pdict.keys(): # 出现一个没有出现的字符，直接清空
                left = right+1 # 而且移到下一个第一个字符
                sdict = {}
            if sdict == pdict:
                ans.append(left)
        return ans

"""
异位词并非代表不重复吧
"""
if __name__ == "__main__":
    s = "cbaebabacd"
    p = "abc"
    print(Solution.findAnagrams(Solution,s,p))