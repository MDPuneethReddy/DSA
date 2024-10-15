import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        for i in range(len(stones)):
            stones[i]=-stones[i]
        heapq.heapify(stones)
        while(True):
            if len(stones)<=1:
                break
            v1=heapq.heappop(stones)
            v2=heapq.heappop(stones)
            if v1!=v2:
                heapq.heappush(stones,v1-v2)
        if len(stones)==0:
            return 0
        else:
            return -stones[0]
        
        
        