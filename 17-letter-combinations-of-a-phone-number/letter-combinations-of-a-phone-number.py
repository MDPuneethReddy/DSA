class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        letters={"2":"abc","3":"def","4":"ghi","5":"jkl","6":"mno","7":"pqrs","8":"tuv","9":"wxyz"}
        l=len(digits)
        if l==0:
            return []
        ind=0
        mainValues=[]
        def recurr(digits,ind,string):
            if ind==l:
                mainValues.append(string)
                return
            for i in letters[digits[ind]]:
                recurr(digits,ind+1,string+i)
            return
        recurr(digits,ind,"")
        return mainValues
                