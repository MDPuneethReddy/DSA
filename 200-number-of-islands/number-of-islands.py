class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited=[[0 for i in range(len(grid[0]))] for _ in range(len(grid))]
        # print(visited)
        count=0
        def dfs(i,j):
            if i<0 or j<0 or i>=len(grid) or j>=len(grid[0]):
                return
            if visited[i][j]==1:
                return
            if grid[i][j]=="0":
                return
            visited[i][j]=1
            # print(visited)
            dfs(i + 1, j)
            dfs(i - 1, j)
            dfs(i, j + 1)
            dfs(i, j - 1)
            return
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if visited[i][j]==0 and grid[i][j]=="1":
                    print("yes",i,j)
                    count+=1
                    dfs(i,j)
        return count
        