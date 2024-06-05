class Solution:
    def climbStairs(self, n: int) -> int:
        self.dic={0:1,1:1}
        def dp(n):
            if n in self.dic:
                return self.dic[n]
            leftValue=0
            rightValue=0
            if n-1 in self.dic:
                leftValue=self.dic[n-1]
                
            else:
                leftValue=dp(n-1)
                self.dic[n-1]=leftValue
            if n-2  in self.dic:
                rightValue=self.dic[n-2]
                
            else:
                rightValue=dp(n-2)
                self.dic[n-2]=rightValue
            return leftValue+rightValue
            
        return dp(n)
            
        
        