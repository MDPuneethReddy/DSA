class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # t-o(n)^2
        # nums=nums1+nums2
        # nums.sort()
        # if(len(nums)%2==0):
        #     return (nums[len(nums)//2]+nums[(len(nums)//2)-1])/2

        # else:
        #     return nums[(len(nums)//2)]

        nums=[]
        
        while(nums1 and nums2):
            if nums1[0]<=nums2[0]:
                nums.append(nums1.pop(0))
            else:
                nums.append(nums2.pop(0))
        # print(nums)
        nums=nums+nums1+nums2
        print(nums)
        if(len(nums)%2==0):
            return (nums[len(nums)//2]+nums[(len(nums)//2)-1])/2

        else:
            return nums[(len(nums)//2)]
        
        