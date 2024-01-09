class MinStack:

    def __init__(self):
        self.stack=[]
        self.mini={-1:math.inf}
        self.index=0
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        self.mini[self.index]=min(self.mini[self.index-1],val)
        self.index+=1
        # print(self.stack,self.mini,self.index)

    def pop(self) -> None:
        del self.mini[self.index-1]
        self.stack.pop()
        self.index-=1
        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.mini[self.index-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()