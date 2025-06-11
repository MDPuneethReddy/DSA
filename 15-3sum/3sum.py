class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        values=[]
        for i in range(len(nums)):
            if i!=0 and nums[i]==nums[i-1]:
                continue
            j=i+1
            k=len(nums)-1
            while(j<k):
                if nums[i]+nums[j]+nums[k]==0:
                    values.append([nums[i],nums[j],nums[k]])
                    while(j<k):
                        if nums[j]==nums[j+1]:
                            j+=1
                        else:
                            break
                    while(j<k):
                        if nums[k]==nums[k-1]:
                            k-=1
                        else:
                            break
                    j+=1
                    k-=1

                elif nums[i]+nums[j]+nums[k]>0:
                    k-=1
                else:
                    j+=1
        return values
                

                    
        