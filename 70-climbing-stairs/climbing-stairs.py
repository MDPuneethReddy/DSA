class Solution:
    def climbStairs(self, n: int) -> int:
        d={1:1,2:2}
        def recurr(n):
            if n==1:
                return 1
            if n==2:
                return 2
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
        