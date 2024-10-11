class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        output=[[-1 for _ in range(n)] for _ in range(m)]
        def recurr(i,j):
            if i<0 or j<0:
                return 0
            if i==0 and j==0:
                return 1
            if output[i][j]!=-1:
                return output[i][j]
            v1=recurr(i-1,j)
            v2=recurr(i,j-1)
            output[i][j]=v1+v2
            return v1+v2
        return recurr(m-1,n-1)
        