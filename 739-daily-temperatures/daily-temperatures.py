class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        values=[0]*len(temperatures)
        stack=[]
        for i in range(len(temperatures)):
            if len(stack)==0:
                stack.append([i,temperatures[i]])
            else:
                while(len(stack)>0):
                    if stack[-1][1]< temperatures[i]:
                        v=stack.pop()
                        values[v[0]]=i-v[0]
                    else:
                        stack.append([i,temperatures[i]])
                        break
                if len(stack)==0:
                    stack.append([i,temperatures[i]])
                # if  stack[-1][0]!=i:
                #     stack.append([i,temperatures[i]])
        for i in stack:
            values[i[0]]=0
        return values