class Solution:
    def climbStairs(self, n: int) -> int:
        # time-o(n) space-o(n)+o(n).   0(n) for recursion stack
        # def recurr(n,dp):
        #     if n<=1:
        #         return 1
        #     if n in dp:
        #         return dp[n]
        #     value= recurr(n-1,dp)+recurr(n-2,dp)
        #     dp[n]=value
        #     return value
        # return recurr(n,{})

        prev1=1
        prev2=1
        for i in range(2,n+1):
            curr=prev1+prev2
            prev2=prev1
            prev1=curr
        return prev1
        