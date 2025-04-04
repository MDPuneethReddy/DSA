class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxi=0
        def recurr(i,j):
            if i<0 or j<0 or i>=len(grid) or j>=len(grid[0]):
                return 0
            if grid[i][j]==0:
                return 0
            grid[i][j]=0
            return 1+recurr(i-1,j)+recurr(i+1,j)+recurr(i,j-1)+recurr(i,j+1)
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==1:
                    maxi=max(maxi,recurr(i,j))
        return maxi
                    
        