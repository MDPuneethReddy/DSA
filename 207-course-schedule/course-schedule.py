class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjacencyList={i:[] for i in range(numCourses)}

        for i in prerequisites:
            adjacencyList[i[1]].append(i[0])
        visited=set()
        pathvisited=set()

        def dfs(source):
            if source in pathvisited:
                return False
            if source in visited:
                return True
            visited.add(source)
            pathvisited.add(source)
            for i in adjacencyList[source]:
                if not dfs(i):
                    return False
            pathvisited.remove(source)
            return True
        for i in range(numCourses):
            if i not in visited:
                if dfs(i)==False:
                    return False
        return True

        