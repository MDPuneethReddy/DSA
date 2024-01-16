class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        l=[]
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue  
            x=i+1
            j=len(nums)-1
            while(x<j):
                # print(x,j)
                if (nums[x]+nums[j]+nums[i])==0:
                    l.append([nums[x],nums[j],nums[i]])
                    while x < j and nums[x] == nums[x + 1]:
                        x += 1  # Skip duplicates
                    while x < j and nums[j] == nums[j - 1]:
                        j -= 1  # Skip duplicates
                    x+=1
                    j-=1
                elif nums[x]+nums[j]+nums[i]>0:
                    j-=1
                else:
                    x+=1
        return l



                
                
        