from typing import List
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = list(list())
        for i in range(numRows+1):
            tmp = list()
            for j in range(i):
                if i > 1: #第三层开始
                    if j-1>=0 and j <= len(res[-1])-1: # 第四层第二个数字哪边不符合了
                        tmp.append((res[-1][j-1]+res[-1][j]))
                    else:
                        tmp.append(1)
                else:
                    tmp.append(1)
            res.append(tmp)
        res.remove([])
        return res

# 1,2,3,4
# 数字关系是在中间，如何dp！看做直角三角形，都是上面层的对应前面两个的和，不满足就1
# [1],
# [1,1],
# [1,2,1],
# [1,3,3,1],
# [1,4,6,4,1]

if __name__ == "__main__":
    numRows = 5
    sol = Solution()
    print(sol.generate(numRows))
