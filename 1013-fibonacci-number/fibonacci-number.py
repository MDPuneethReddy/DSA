class Solution:
    def fib(self, n: int) -> int:
        d={0:0,1:1}
        def recurr(n):
            if n==0:
                return 0
            if n==1:
                return 1
            if n-1 in d:
                v=d[n-1]
            else:
                v=recurr(n-1)
                d[n-1]=v
            if n-2 in d:
                v1=d[n-2]
            else:
                v1=recurr(n-2)
                d[n-2]=v1
            return v+v1
        return recurr(n)

        