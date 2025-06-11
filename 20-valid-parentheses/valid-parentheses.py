class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        for i in s:
            if i in ["(","{","["]:
                stack.append(i)
            else:
                if i==")":
                    if len(stack)<=0:
                        return False
                    else:
                        if stack[-1]!="(":
                            return False
                        else:
                            stack.pop()
                elif i=="]":
                    if len(stack)<=0:
                        return False
                    else:
                        if stack[-1]!="[":
                            return False
                        else:
                            stack.pop()
                elif i=="}":
                    if len(stack)<=0:
                        return False
                    else:
                        if stack[-1]!="{":
                            return False
                        else:
                            stack.pop()
        if len(stack)>0:
            return False
        return True
        