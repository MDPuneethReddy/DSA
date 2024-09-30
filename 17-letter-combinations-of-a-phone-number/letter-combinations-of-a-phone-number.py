class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        letters={"2":"abc","3":"def","4":"ghi","5":"jkl","6":"mno","7":"pqrs","8":"tuv","9":"wxyz"}
        l=len(digits)
        if l==0:
            return []
        ind=1
        mainValue=[i for i in letters[digits[0]]]
        def recurr(digits,ind,l,mainValue):
            if ind==l:
                return mainValue
            values=[]
            for j in mainValue:
                for k in letters[digits[ind]]:
                    values.append(j+k)
            mainValue=values
            return recurr(digits,ind+1,l,mainValue)
            
        return recurr(digits,ind,l,mainValue)
                

    

        