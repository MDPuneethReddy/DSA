class Solution:
    def trap(self, height: List[int]) -> int:
        maxleft=height[0]
        maxright=height[len(height)-1]
        left=0
        right=len(height)-1
        total=0
        while(left<right):
            if maxleft<=maxright:
                val=maxleft-height[left]
                if val>0:
                    total+=val
                left+=1
                maxleft=max(maxleft,height[left])
            else:
                val=maxright-height[right]
                if val>0:
                    total+=val
                right-=1
                maxright=max(maxright,height[right])
        return total
            


        