class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def dfs(grid,i,j,gridl,gridh):
            
            if i<0 or i>=gridl or j<0 or j>=gridh:
                return 0
            if grid[i][j]==0:
                return 0
            if (i,j) in visited:
                return 0
            visited.add((i,j))
            return 1+ dfs(grid,i-1,j,gridl,gridh)+dfs(grid,i+1,j,gridl,gridh)+dfs(grid,i,j+1,gridl,gridh)+dfs(grid,i,j-1,gridl,gridh)
        

        visited=set()
        i=0
        j=0
        gridl=len(grid)
        gridh=len(grid[0])
        self.maxicount=0
        for i in range(gridl):
            for j in range(gridh):
                if grid[i][j]==1:
                    count=dfs(grid,i,j,gridl,gridh)
                    self.maxicount=max(count,self.maxicount)
        
        return self.maxicount
        