class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        output=[0]*len(temperatures)
        stack=[]
        for i in range(len(temperatures)):
            if len(stack)==0:
                stack.append([temperatures[i],i])
            else:
                while(1):
                    if len(stack)>0 and stack[-1][0]<temperatures[i]:
                        val=stack.pop()
                        output[val[1]]=i-val[1]
                    else:
                        break
                stack.append([temperatures[i],i])
        return output

        