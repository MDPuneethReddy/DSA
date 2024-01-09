class Solution:
    def maxArea(self, height: List[int]) -> int:
        #time-o(n) space-o(1)
        i=0
        j=len(height)-1
        maxi=-math.inf
        while(i<j):
            val=min(height[j],height[i])
            maxi=max(maxi,val*abs(j-i))
            # print(val,maxi)
            if height[i]<height[j]:
                i+=1
            else:
                j-=1
        return maxi
        