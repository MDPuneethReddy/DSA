class Solution:
    def climbStairs(self, n: int) -> int:
        def recurr(n,dp):
            if n<=1:
                return 1
            if n in dp:
                return dp[n]
            value= recurr(n-1,dp)+recurr(n-2,dp)
            dp[n]=value
            return value
        return recurr(n,{})
        