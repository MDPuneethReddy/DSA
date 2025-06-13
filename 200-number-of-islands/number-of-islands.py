class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited=set()
        count=0
        lenGridX=len(grid)
        lenGridY=len(grid[0])
        def findadjacentones(i,j):
            if i<0 or i>=lenGridX or j<0 or j>=lenGridY:
                return
            if (i,j) in visited:
                return
            if grid[i][j]=="0":
                return
            visited.add((i,j))
            findadjacentones(i+1,j)
            findadjacentones(i-1,j)
            findadjacentones(i,j+1)
            findadjacentones(i,j-1)
            return
        for i in range(lenGridX):
            for j in range(lenGridY):
                if grid[i][j]=="1":
                    if (i,j) not in visited:
                        count+=1
                        findadjacentones(i,j)
        return count


        