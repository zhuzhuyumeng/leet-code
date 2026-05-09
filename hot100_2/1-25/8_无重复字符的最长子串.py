class Solution:
    def lengthOfLongestSubstring(self, s:str)->int:
        hashtable = {}
        n = len(s)
        left = 0
        maxsize = 0
        for i in range(n):
            hashtable[s[i]] = hashtable.get(s[i],0)+1
            while hashtable[s[i]]==2:
                hashtable[s[left]] = hashtable[s[left]]-1
                if hashtable[s[left]] == 0:
                    hashtable.pop(s[left])
                left += 1
            maxsize = max(maxsize,len(hashtable))
        return maxsize

    def lengthOfLongestSubstringSet(self, s: str) -> int:
        occ = set()
        n = len(s)
        left = 0
        ans = 0
        for right in range(n):
            while s[right] in occ:
                occ.remove(s[left]) # 移除之前的元素，直到让right元素补充进去
                left += 1
            occ.add(s[right])
            ans  = max(ans,len(occ))
        return ans
"""
滑动窗口的时候如何统计字符出现的次数？真是hash
"""
if __name__== "__main__":
    s = "abcabcbb"
    s = "pwwkew"
    # print(Solution.lengthOfLongestSubstring(Solution,s))
    print(Solution.lengthOfLongestSubstringSet(Solution, s))