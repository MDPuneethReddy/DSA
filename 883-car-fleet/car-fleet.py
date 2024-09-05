class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        mainList=[]
        for i in range(len(position)):
            time=(target-position[i])/speed[i]
            mainList.append([position[i],speed[i],time])
        mainList.sort(key=lambda x:(x[0]))
        count=0
        stack=[]
        for i in range(len(mainList)):
            value=mainList[len(mainList)-i-1]
            if len(stack)==0:
                stack.append(value)
            else:
                if stack[-1][2]<value[2]:
                    count+=1
                    stack.pop()
                    stack.append(value)
        if len(stack)>0:
            count+=1
        return count
        