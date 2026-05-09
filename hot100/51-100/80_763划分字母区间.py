from typing import List
class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last = [0]*26
        for i,ch in enumerate(s):
            last[ord(ch)-ord("a")] = i #这样a就在0了

        start = 0
        end = 0
        res = list()
        for i,ch in enumerate(s):
            end = max(end,last[ord(ch)-ord("a")])
            if i == end: #如果当前位置=最晚出现的位置，就有了一组
                res.append(end-start+1) # 9-0是十个数字
                start = end + 1
        return res

# 每个字母都记录起始位置和结束位置
# 如果每个字母对应他的最后下标
# 返回的是区间的长度

if __name__ == "__main__":
    s = "ababcbacadefegdehijhklij"
    sol = Solution()
    print(sol.partitionLabels(s))