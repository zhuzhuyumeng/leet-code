class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [0]*2
        dp[0] = 1
        if n==1:
            return dp[0]
        dp[1] = 2
        for i in range(3,n+1):
            tmp = dp[0]+dp[1]
            dp[0] = dp[1]
            dp[1] = tmp
        return dp[1]

if __name__ == "__main__":
    n = 3
    sol = Solution()
    print(sol.climbStairs(n))