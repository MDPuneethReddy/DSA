class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if len(nums)==0:
            return []
        if len(nums)==1:
            return [str(nums[0])]
        mainList=[]
        stack=[]
        for i in range(len(nums)):
            if len(stack)==0:
                stack.append(nums[i])
            else:
                if (stack[-1]+1)==nums[i]:
                    stack.append(nums[i])
                else:
                    if len(stack)==0:
                        mainList.append("")
                    if len(stack)==1:
                        mainList.append(str(stack[-1]))
                        stack=[]
                    else:
                        mainList.append(str(stack[0])+"->"+str(stack[-1]))
                        stack=[]
                    stack.append(nums[i])
        if len(stack)!=0:
            
            if len(stack)==1:
                mainList.append(str(stack[-1]))
            else:
                mainList.append(str(stack[0])+"->"+str(stack[-1]))
        return mainList
            
                
        