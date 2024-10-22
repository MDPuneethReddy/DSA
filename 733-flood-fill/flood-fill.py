class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        # visited=[[0 for i in range(len(image[0]))] for _ in range(len(image))]
        def dfs(i,j,initialColor):
            if i<0 or j<0 or i>=len(image) or j>=len(image[0]):
                return
            # if visited[i][j]==1:
            #     return
            if image[i][j]!=initialColor or image[i][j]==color:
                return
            # visited[i][j]=1
            image[i][j]=color
            dfs(i-1,j,initialColor)
            dfs(i,j-1,initialColor)
            dfs(i+1,j,initialColor)
            dfs(i,j+1,initialColor)
            return
        initalColor=image[sr][sc]
        # image[sr][sc]=color
        dfs(sr,sc,initalColor)
        return image

        