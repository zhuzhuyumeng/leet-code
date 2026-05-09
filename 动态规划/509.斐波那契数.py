class Solution:
    def fib(self, n: int) -> int:
        dp = [0]*2
        dp[0] = 0
        dp[1] = 1
        for i in range(2,n+1):
            tmp = dp[0]+dp[1]
            dp[0] = dp[1]
            dp[1] = tmp
        return dp[1]
        # list = [0]*(n+1)
        # list[0] = 0
        # list[1] = 1
        # count = 0
        # for i in range(2 ,n+1):
        #     list[i] = list[i-1]+list[i-2]
        # count = list[-1]
        # return count

if __name__ == "__main__":
    n = 4
    sol = Solution()
    print(sol.fib(n))