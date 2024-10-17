import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heapArr=[]
        heapq.heapify(heapArr)
        for i in points:
            d=math.sqrt(abs(i[0]*i[0])+abs(i[1]*i[1]))
            heapq.heappush(heapArr,(d,i[0],i[1]))
        values=[]
        for i in range(k):
            value=heapq.heappop(heapArr)
            values.append([value[1],value[2]])
        return values
        