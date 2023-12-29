class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d={}
        for i in nums:
            if i not in d:
                d[i]=1
            else:
                d[i]+=1
        values=[]
        for i in range(k):
            maxi=-math.inf
            key=0
            for i in d:
                if d[i]>=maxi:
                    maxi=max(maxi,d[i])
                    key=i
            values.append(key)
            del d[key]

        return values
        