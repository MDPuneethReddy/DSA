class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        d={}
        for i in range(len(edges)):
            if edges[i][0] in d:
                d[edges[i][0]].append(edges[i][1])
                if edges[i][1] in d:
                    d[edges[i][1]].append(edges[i][0])
                else:
                    d[edges[i][1]]=[edges[i][0]]
            else:
                d[edges[i][0]]=[edges[i][1]]
                if edges[i][1] in d:
                    d[edges[i][1]].append(edges[i][0])
                else:
                    d[edges[i][1]]=[edges[i][0]]
                
        
        # print(d)
        def dfs(d,source,destination,boolean=False,visited=[0]*n):
            # print("bbol",d,source,destination)
            if (source==destination):
                return True
            if boolean==True:
                visited=[1]*n
            if visited[source]==1:
                return False
            else:
                
                visited[source]=1
                for i in range(len(d[source])):
                    boolean=boolean or dfs(d,d[source][i],destination,boolean,visited)
            return boolean
        return dfs(d,source,destination)
        
        # d={}
        # if edges==[]:
        #     return True
        # for i in range(len(edges)):
        #     if edges[i][0] in d:
        #         d[edges[i][0]].append(edges[i][1])
        #         if edges[i][1] in d:
        #             d[edges[i][1]].append(edges[i][0])
        #         else:
        #             d[edges[i][1]]=[edges[i][0]]
        #     else:
        #         d[edges[i][0]]=[edges[i][1]]
        #         if edges[i][1] in d:
        #             d[edges[i][1]].append(edges[i][0])
        #         else:
        #             d[edges[i][1]]=[edges[i][0]]
        # self.bool=False
        # self.visited=[]
        # def recurr(d,source,destination):
        #     if source not in d:
        #         return 
        #     if source in self.visited:
        #         return
        #     self.visited.append(source)
        #     if source==destination:
        #         self.bool=True
        #     for i in d[source]:
        #         recurr(d,i,destination)
        #     return
        # recurr(d,source,destination)
        # return self.bool        