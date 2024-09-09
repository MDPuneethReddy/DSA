class Solution:
    def romanToInt(self, s: str) -> int:
        d={"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        total=0
        stack=[]
        for i in range(len(s)):
            v=s[len(s)-i-1]
            if len(stack)==0:
                stack.append(v)
            else:
                if stack[-1]in ["X","V"] and v=="I":
                    if stack[-1]=="X":
                        total+=9
                    elif stack[-1]=="V":
                        total+=4
                    stack.pop()
                
                elif stack[-1] in ["L","C"] and v=="X":
                    if stack[-1]=="L":
                        total+=40
                    elif stack[-1]=="C":
                        total+=90
                    stack.pop()
                
                elif stack[-1] in ["D","M"] and v=="C":
                    if stack[-1]=="D":
                        total+=400
                    elif stack[-1]=="M":
                        total+=900
                    stack.pop()
                else:
                    total+=d[stack.pop()]
                    stack.append(v)
        if len(stack)>0:
            total+=d[stack[-1]]
        return total


        