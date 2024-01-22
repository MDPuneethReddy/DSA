class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        values=[0]*len(temperatures)
        stack=[]
        for i in range(len(temperatures)):
            while(1):
                if len(stack)==0:
                    stack.append([temperatures[i],i])
                    break
                v=stack[-1]
                if(v[0]<temperatures[i]):
                    v1=stack.pop()
                    values[v1[1]]=abs(v1[1]-i)
                else:
                    stack.append([temperatures[i],i])
                    break
        return values

        