class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        mainList=[]
        def recurr(left,right,mainList,s):
            if left==0 and right==0:
                mainList.append(s)
                print(s)
                return mainList
            if left>0:
                recurr(left-1,right,mainList,s+"(")
            if right>left:
                recurr(left,right-1,mainList,s+")")
            return mainList
        return recurr(n,n,[],"")
        # return mainList
        