class Solution:
    def myPow(self, x: float, n: int) -> float:
        def helper(x,n):
            if n==0:
                return 1
            if x==0:
                return 0
            res=helper(x,n//2)
            val=res*res
            if n%2==0:
                return val
            else:
                return val*x
            
        res=helper(x,abs(n))
        if n>=0:
            return res
        else:
            return 1/res

        