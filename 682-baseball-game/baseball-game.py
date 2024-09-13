class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack=[]
        total=0
        def checknumber(num):
            try:
                v=float(num)
                return True
            except ValueError:
                return False
        for i in operations:
            if checknumber(i):
                stack.append(int(i))
                total+=int(i)
            elif i=="C":
                v=stack.pop()
                total-=v
            elif i=="D":
                total+=stack[-1]*2
                stack.append(stack[-1]*2)
            elif i=="+":
                v=stack[-1]+stack[-2]
                total+=v
                stack.append(v)
            else:
                return "invalid"
        return total
                

        