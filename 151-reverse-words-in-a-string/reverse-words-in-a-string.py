class Solution:
    def reverseWords(self, s: str) -> str:
        stack=[]
        for i in s:
            if len(stack)==0:
                if i!=" ":
                    stack.append(i)
            else:
                if i==" ":
                    if stack[-1]!=" ":
                        stack.append(i)
                else:
                    stack.append(i)
        mainString=""
        s=""
        while(stack):
           
            v=stack.pop()
            if v==" ":
                if s!="":
                    mainString+=s
                    s=""
                    mainString+=" "
                
            else:
                s=v+s
        mainString+=s
        print(mainString)
        return mainString
        