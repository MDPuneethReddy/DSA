class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        array=[0]*len(nums)
        index=len(nums)-1
        i=0
        j=len(nums)-1
        while(i<=j):
            if abs(nums[i])>=abs(nums[j]):
                array[index]=nums[i]*nums[i]
                i+=1
            else:
                array[index]=nums[j]*nums[j]
                j-=1
            index-=1
        return array
        