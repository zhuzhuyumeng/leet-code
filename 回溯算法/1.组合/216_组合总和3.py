class Solution:
    def combinationSum3(self, k: int, n: int) -> list[list[int]]:
        def backtracking(start:int,k: int,count:int):
            if k==0 and count==n:
                res.append(tmp.copy())
                return
            if count>n:
                return
            if k<-1:
                return
            if k>n-start+1:#当前需要的数字数量大于还剩下的数量
                return
            for i in range(start,10):
                tmp.append(i)
                backtracking(i+1,k-1,count+i)
                tmp.pop()

        tmp = []
        res = []
        backtracking(1,k,0)
        return res


if __name__ == '__main__':
    n = 2
    k = 18
    soulution = Solution()
    res = soulution.combinationSum3(n,k)
    print(res)