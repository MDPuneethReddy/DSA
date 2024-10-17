import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d={}
        for i in nums:
            if i not in d:
                d[i]=1
            else:
                d[i]+=1
        heapArr=[]
        heapq.heapify(heapArr)
        for key,value in d.items():
            heapq.heappush(heapArr,(-value,key))
        values=[]
        for i in range(k):
            v=heapq.heappop(heapArr)
            values.append(v[1])
        return values
        