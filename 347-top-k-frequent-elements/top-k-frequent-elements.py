class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #learn what is meant by bucket sort
        d={}
        for i in nums:
            if i not in d:
                d[i]=1
            else:
                d[i]+=1
        l = [[] for _ in range(len(nums))]
        for i in d:
            l[d[i]-1].append(i)
        values=[]
        for i in range(len(nums)):
            if(nums[len(nums)-i-1]!=[]):
                for j in l[len(nums)-i-1]:
                    values.append(j)
                    k-=1
                    print(values,k)
                    if(k<=0):
                        return values
        
        