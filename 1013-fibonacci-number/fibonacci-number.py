class Solution:
    def fib(self, n: int) -> int:
        d={0:0,1:1}
        for i in range(2,n+1):
            v=d[i-1]+d[i-2]
            d[i]=v
        return d[n]