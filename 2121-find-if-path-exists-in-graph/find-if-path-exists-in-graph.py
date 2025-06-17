class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        hashmap={}
        for i in edges:
            if i[0] in hashmap:
                hashmap[i[0]].append(i[1])
            else:
                hashmap[i[0]]=[i[1]]
            if i[1] in hashmap:
                hashmap[i[1]].append(i[0])
            else:
                hashmap[i[1]]=[i[0]]

        visited=set()
        self.found=False
        def findpath(source,destination,hashmap):
            if source==destination:
                self.found=True
                return 
            if source not in hashmap:
                return
            visited.add(source)
            for i in hashmap[source]:
                if i not in visited:
                    findpath(i,destination,hashmap)
            return
        findpath(source,destination,hashmap)
        return self.found
        


        
        