class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        init=len(cost)
        d={0:cost[0],1:cost[1]}
        for i in range(2,len(cost)+1):
            v=min(d[i-1],d[i-2])
            if i<=len(cost)-1:
                v+=cost[i]
            d[i]=v
        return d[init]