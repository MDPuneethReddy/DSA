import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #use bucker sort for o(n)
        d={}
        for i in nums:
            if i not in d:
                d[i]=1
            else:
                d[i]+=1
        values=[[] for _ in range(len(nums)+1)]
        for key,value in d.items():
            values[value].append(key)
        mainValues=[]
        for i in range(len(values)-1,-1,-1):
            if len(values[i])>0:
                while(k>0 and len(values[i])>0):
                    mainValues.append(values[i].pop())
                    k-=1
        return mainValues



        #klogn time complexity using heap
        # d={}
        # for i in nums:
        #     if i not in d:
        #         d[i]=1
        #     else:
        #         d[i]+=1
        # heapArr=[]
        # heapq.heapify(heapArr)
        # for key,value in d.items():
        #     heapq.heappush(heapArr,(-value,key))
        # values=[]
        # for i in range(k):
        #     v=heapq.heappop(heapArr)
        #     values.append(v[1])
        # return values
        