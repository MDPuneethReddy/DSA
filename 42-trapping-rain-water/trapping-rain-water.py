class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height)==0:
            return 0
        leftmax=[]
        rightmax=[0]*len(height)
        lmax=0
        rmax=0
        for i in range(len(height)):
            leftmax.append(lmax)
            lmax=max(lmax,height[i])
        for i in range(len(height)-1,-1,-1):
            rightmax[i]=rmax
            rmax=max(rmax,height[i])
        count=0
        for i in range(len(height)):
                count += min(leftmax[i], rightmax[i]) - height[i] if min(leftmax[i], rightmax[i]) - height[i] >= 0 else 0

        return count

        #time complexity -o(n), space- o(1)
        # if len(height)==0 :
        #     return 0
        # l,r=0,len(height)-1
        # leftmax=height[l]
        # rightmax=height[r]
        # res=0
        # while(l<r):
        #     if leftmax<=rightmax:
        #         l+=1
        #         leftmax=max(leftmax,height[l])
        #         if (leftmax-height[l]>0):
        #             res+=leftmax-height[l]
        #     else:
        #         r-=1
        #         rightmax=max(rightmax,height[r])
        #         if (rightmax-height[r]>0):
        #             res+=rightmax-height[r]
        # return res

        