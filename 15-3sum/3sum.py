class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        mainList=[]
        nums.sort()
        for i in range(len(nums)):
            if i>0 and nums[i]==nums[i-1]:
                continue
            x=nums[i]
            y=i+1
            z=len(nums)-1
            while(y<z):
                if x+nums[y]+nums[z]==0:
                    mainList.append([x,nums[y],nums[z]])
                    while y < z and nums[y] == nums[y + 1]:
                        y += 1
                    while y < z and nums[z] == nums[z - 1]:
                        z -= 1
                    y+=1
                    z-=1
                elif x+nums[y]+nums[z]<0:
                    y+=1
                else:
                    z-=1
        return mainList

        