class Solution:
    def combine(self, n: int, k: int) -> list[list[int]]:
        def backtracking(start: int,k: int):
            if k==0:
                res.append(tmp.copy())
                return
            if start>n:
                return
            if k<0:
                return
            for i in range(start,n+1):
                tmp.append(i)
                backtracking(i+1,k-1)
                tmp.pop()


        tmp = []
        res = []
        start = 1
        backtracking(start,k)
        return res


        # def backtracking(start:int,n: int,k: int,res: list[list[int]],tmp: list[int] ):
        #     if k==0:
        #         res.append(tmp.copy())
        #         return
        #     for i in range(start,n+1):
        #         if i not in tmp:
        #             tmp.append(i)
        #             backtracking(i,n,k-1,res,tmp)
        #             tmp.pop()
        # res = []
        # tmp = []
        # backtracking(1,n,k,res,tmp)
        # return res

if __name__ == '__main__':
    n = 4
    k = 1
    soulution = Solution()
    res = soulution.combine(n,k)
    print(res)