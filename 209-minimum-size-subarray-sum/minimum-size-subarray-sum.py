class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        i=0
        j=0
        s=0
        maxlength=math.inf
        while(j<len(nums)):
            s+=nums[j]
            if s>=target:
                maxlength=min(maxlength,j-i+1)
                while(i<=j):
                    s-=nums[i]
                    i+=1
                    if s>=target:
                        maxlength=min(maxlength,j-i+1)
                    else:
                        break

            j+=1
        if maxlength==math.inf:
            return 0
        return maxlength

        