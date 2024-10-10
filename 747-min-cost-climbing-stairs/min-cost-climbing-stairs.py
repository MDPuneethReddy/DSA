class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        init=len(cost)
        d={0:cost[0],1:cost[1]}
        def recurr(init,s):
            if init==1:
                return cost[1]
            elif init==0:
                return cost[0]
            if init-1 in d:
                v1=d[init-1]
            else:
                v1=recurr(init-1,s)
                d[init-1]=v1
            if init-2 in d:
                v2=d[init-2]
            else:
                v2=recurr(init-2,s)
                d[init-2]=v2
            v= min(v1,v2)
            if init<=len(cost)-1:
                s+=cost[init]
            return s+v
        return recurr(init,0)
        