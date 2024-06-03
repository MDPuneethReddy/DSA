class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        def findsubsets(inp,inputNums,output):
            output.append(inp.copy())
            if inputNums==[]:
                return output
            for i in range(len(inputNums)):
                inp.append(inputNums[i])
                findsubsets(inp,inputNums[i+1:],output)
                inp.pop()
            return output
        return findsubsets([],nums,[])
        