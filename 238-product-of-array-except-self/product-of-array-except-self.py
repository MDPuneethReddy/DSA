class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        c=0
        for i in nums:
            if i==0:
                c+=1
        if c>1:
            return [0]*len(nums)
        elif c==1:
            product=1
            for i in nums:
                if i!=0:
                    product*=i
            l=[]
            for i in nums:
                if i!=0:
                    l.append(0)
                else:
                    l.append(product)
            return l
        else:

            product=1
            for i in nums:
                product*=i
            l=[]
            for i in nums:
                l.append(product//i)
            return l
        