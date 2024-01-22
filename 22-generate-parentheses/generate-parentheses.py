class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        l=[]
        def recurssion(open,close,s):
            # print(open,close,s)
            if open==0 and close==0:
                # print(open,close,s)
                l.append(s)
                return
            if(open<close):
                if(open>0):
                    recurssion(open-1,close,s+"(") 
                if(close>0):
                    recurssion(open,close-1,s+")")
            if(open==close):
                recurssion(open-1,close,s+"(") 
            return
        recurssion(n,n,"")
        return l
            
            
            
        