class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        d={}
        if edges==[]:
            return True
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
        self.bool=False
        self.visited=[0]*n
        def recurr(d,source,destination):
            if source not in d:
                return 
            if self.visited[source]==1:
                return
            self.visited[source]=1
            if source==destination:
                self.bool=True
            for i in d[source]:
                recurr(d,i,destination)
            return
        recurr(d,source,destination)
        return self.bool        