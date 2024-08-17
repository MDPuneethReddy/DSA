class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # #with division
        # c=0
        # for i in nums:
        #     if i==0:
        #         c+=1
        # if c>1:
        #     return [0]*len(nums)
        # elif c==1:
        #     product=1
        #     for i in nums:
        #         if i!=0:
        #             product*=i
        #     l=[]
        #     for i in nums:
        #         if i!=0:
        #             l.append(0)
        #         else:
        #             l.append(product)
        #     return l
        # else:

        #     product=1
        #     for i in nums:
        #         product*=i
        #     l=[]
        #     for i in nums:
        #         l.append(product//i)
        #     return l
        


        #without division
        left=[]
        right=[0]*len(nums)
        lp=1
        for i in nums:
            lp*=i
            left.append(lp)
        rp=1
        for i in range(len(nums)):
            rp*=nums[len(nums)-i-1]
            right[len(nums)-i-1]=rp
        # print(left,right)
        l=[]
        for i in range(len(nums)):
            if i==0:
                l.append(right[1])
            elif i==len(nums)-1:
                l.append(left[len(nums)-2])
            else:
                l.append(left[i-1]*right[i+1])
        return l


        