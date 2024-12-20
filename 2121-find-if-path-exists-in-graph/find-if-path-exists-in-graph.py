class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        d={}
        for i in range(len(edges)):
            if edges[i][0] not in d:
                d[edges[i][0]]=[edges[i][1]]
            else:
                d[edges[i][0]].append(edges[i][1])
            if edges[i][1] not in d:
                d[edges[i][1]]=[edges[i][0]]
            else:
                d[edges[i][1]].append(edges[i][0])
        #dfs
        visited=[0]*n
        def recurr(entry):
            # print(entry)
            if entry==destination:
                # print("yes")
                return True
            if visited[entry]==1:
                return False
            visited[entry]=1
            found=False
            for i in range(len(d[entry])):
                if visited[d[entry][i]]==0:
                    print(d[entry][i])
                    found=found or recurr(d[entry][i])
            return found
        return recurr(source)
            

        





        # bfs
        # queue=[source]
        # visited=[0]*n
        # found=False
        # # print(d)
        # while(queue):
        #     v=queue.pop(0)
        #     if v==destination:
        #         found=True
        #         break
        #     if visited[v]==0:
        #         visited[v]=1
            
        #         for i in range(len(d[v])):
        #             queue.append(d[v][i])
        #         # print(v,queue,visited)
        # return found


        