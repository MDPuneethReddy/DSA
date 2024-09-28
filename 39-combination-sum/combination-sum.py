class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        mainList=set()
        def recurr(candidates,target,s,ind,l):
            # print(s,ind,l)
            if s>target:
                return
            if s==target:
                mainList.add(tuple(l[:]))
                return
            if ind>=len(candidates):
                if s==target:
                    mainList.add(tuple(l[:]))
                return
            recurr(candidates,target,s,ind+1,l)
            l.append(candidates[ind])
            recurr(candidates,target,s+candidates[ind],ind,l)
            recurr(candidates,target,s+candidates[ind],ind+1,l)
            l.pop()
            return
        recurr(candidates,target,0,0,[])
        return list(mainList)
        
            
            

        