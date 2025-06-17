class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adjacencylist={i:[] for i in range(numCourses)}
        for i in prerequisites:
            adjacencylist[i[1]].append(i[0])
        visited=set()
        pathvisited=set()
        output=[]
        cycleDetected=False
        def dfs(source):
            if source in pathvisited:
                return True
            if source in visited:
                return False
            visited.add(source)
            pathvisited.add(source)
            for i in adjacencylist[source]:
                if dfs(i) ==True:
                    return True
            output.append(source)
            pathvisited.remove(source)
            return False

        for i in range(numCourses):
            if i not in visited and not cycleDetected:
                if dfs(i):
                    cycleDetected=True
                    return []
        return output[::-1]

        