class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def findall(candidates,target,output,index,mainOutput):
            if target==0:
                mainOutput.append(output.copy())
                return
            if target<0:
                return
            for i in range(index,len(candidates)):
                output.append(candidates[i])
                findall(candidates,target-candidates[i],output,i,mainOutput)
                output.pop()
            return mainOutput
        
            

        
        return findall(candidates,target,[],0,[])
        