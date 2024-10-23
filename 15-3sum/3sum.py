class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        mainList=[]
        for i in range(len(nums)):
            if i!=0 and nums[i]==nums[i-1]:
                continue
            else:
                y=i+1
                z=len(nums)-1
                while(y<z):
                    cs=nums[i]+nums[y]+nums[z]
                    if cs==0:
                        mainList.append([nums[i],nums[y],nums[z]])
                        while y<z and nums[y]==nums[y+1]:
                            y+=1
                        while y<z and nums[z]==nums[z-1]:
                            z-=1
                        y+=1
                        z-=1
                    elif cs<0:
                        y+=1
                    else:
                        z-=1
        return mainList
        