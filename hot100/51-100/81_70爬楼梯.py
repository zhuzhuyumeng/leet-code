class Solution:
    def climbStairs(self, n: int) -> int:
        p = 1
        q = 2
        if n == 1:
            return p
        elif n == 2:
            return q
        else:
            for i in range(3,n+1):
                r = p+q # 每一步都是在前一步的基础上
                p = q
                q = r
        return r
        # def dfs(taijie:int):
        #     if taijie==0 :
        #         return 1
        #     if taijie<0 :
        #         return 0
        #     return dfs(taijie-1)+dfs(taijie-2)
        # print(dfs(n))


if __name__ == "__main__":
    n = 3
    sol = Solution()
    print(sol.climbStairs(n))