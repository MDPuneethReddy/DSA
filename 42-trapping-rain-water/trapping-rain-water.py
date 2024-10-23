class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height)==0 :
            return 0
        l,r=0,len(height)-1
        leftmax=height[l]
        rightmax=height[r]
        res=0
        while(l<r):
            if leftmax<=rightmax:
                l+=1
                leftmax=max(leftmax,height[l])
                if (leftmax-height[l]>0):
                    res+=leftmax-height[l]
            else:
                r-=1
                rightmax=max(rightmax,height[r])
                if (rightmax-height[r]>0):
                    res+=rightmax-height[r]
        return res

        