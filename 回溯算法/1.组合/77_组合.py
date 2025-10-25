class Solution:
    def combine(self, n: int, k: int) -> list[list[int]]:
        def backtracking(cur:int, n:int):
            if cur == n:
                res.append(tmp)
                return
            tmp.append()

        tmp = []


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
    k = 2
    soulution = Solution()
    res = soulution.combine(n,k)
    print(res)