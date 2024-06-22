class Solution:
    def fib(self, n: int) -> int:
        dp={}
        def recurr(n):
            if n<=1:
                return n
            if n in dp:
                return dp[n]
            value= recurr(n-1)+recurr(n-2)
            dp[n]=value
            return value
        return recurr(n)
            
        