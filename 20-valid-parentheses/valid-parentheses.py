class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        for i in s:
            if i in ["(","{","["]:
                stack.append(i)
            else:
                if len(stack)==0:
                    return False
                v=stack.pop()
                if (v!="(" and i==")") or (v!="[" and i=="]") or (v!="{" and i=="}"):
                    return False
        if len(stack)>0:
            return False
        return True
        