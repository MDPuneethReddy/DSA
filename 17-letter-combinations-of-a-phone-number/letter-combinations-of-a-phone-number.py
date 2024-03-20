class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        letters={
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }
        values=[]
        for i in digits:
            values.append(letters[i])
        if len(digits)==0:
            return []
        elif len(digits)==1:
            return [x for x in letters[digits[0]]]
        else:
            result=[]
            while(len(values)>1):
                value=[]
                v1=values.pop()
                v2=values.pop()
                for j in range(len(v1)):
                    for k in range(len(v2)):
                        value.append(v2[k]+v1[j])
                values.append(value)
            # print(values)


            
        return values[0]
        