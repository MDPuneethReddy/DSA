class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        visited=[0]*len(isConnected)
        count=0
        def dfs(index):
            if visited[index]==1:
                return
            visited[index]=1
            for i in range(len(isConnected[index])):
                # print(isConnected[index][i]!=0,i!=index,visited[i]==0)
                if isConnected[index][i]==1 and i!=index and visited[i]==0:
                    # print(i)
                    dfs(i)
            return

        while(sum(visited)!=len(visited)):
            
            # print(count,visited)
            for i in range(len(visited)):
                if visited[i]==0:
                    count+=1
                    dfs(i)
                # print(visited)
        return count
        