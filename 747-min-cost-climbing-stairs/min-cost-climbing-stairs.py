class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        l=len(cost)
        cost.append(0)
        mem={}
        def recurr(cost,index,su):
            if index in mem:
                return mem[index]
            if index<0:
                return 0
            if index>=0 and index<=1:
                return cost[index]
            su=cost[index]
            left=recurr(cost,index-1,su)
            right=recurr(cost,index-2,su)
            su+=min(left,right)
            mem[index]=su
            return su
        return recurr(cost,l,0)

          

        

       
            
        