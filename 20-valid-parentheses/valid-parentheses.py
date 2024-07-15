class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        for i in range(len(s)):
            if s[i] in ["(","{","["]:
                stack.append(s[i])
            else:
                if len(stack)==0:
                    return False
                v=stack.pop()
                if v in ["}","]",")"]:
                    return False
                # print(v,s[i])
                if v=="(" and s[i] in ["}","]"]:
                    return False
                if v=="{" and s[i] in [")","]"]:
                    return False
                if v=="[" and s[i] in ["}",")"]:
                    return False
        if len(stack)>0:
            return False
        return True
                
        