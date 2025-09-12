class Solution:
    def findAnagrams(self, s: str, p: str) -> list[int]:
        s_length = len(s)
        p_length = len(p)
        hash_map = dict()
        llist = []
        for i in range(s_length):
            left = 0
            right = p_length-1
            if s[i]==p[left]:
                j=i
                while left<=right and s[j]==p[left] :
                    left+=1
                    j+=1
                if left>right:
                    llist.append(i)
                left = 0
            elif s[i]==p[right]:
                j=i
                while right>=left and s[j]==p[right] and j<=s_length-2:
                    right-=1
                    j+=1
                if right<left:
                    llist.append(i)
                right = p_length - 1
        return llist



# s = "cbaebabacd"
# p = "abc"
s = "abab"
p = "ab"
print(Solution.findAnagrams(Solution, s,p))