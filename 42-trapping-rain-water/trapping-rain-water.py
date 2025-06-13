class Solution:
    def trap(self, height: List[int]) -> int:
        maxleft=0
        maxright=0
        left=[]
        right=[0]*len(height)
        for i in range(len(height)):
            left.append(maxleft)
            maxleft=max(maxleft,height[i])
        for i in range(len(height)):
            right[len(height)-i-1]=maxright
            maxright=max(maxright,height[len(height)-i-1])
        total=0
        for i in range(len(height)):
            val=min(left[i],right[i])-height[i]
            if val>0:
                total+=val
        return total

        