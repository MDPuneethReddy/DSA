class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        mainResult=[]
        def recurr(n,k,ind,l):
            if ind>n:
                if len(l)==k:
                    mainResult.append(l[:])
                return
            if len(l)==k:
                mainResult.append(l[:])
                return
            recurr(n,k,ind+1,l)
            l.append(ind)
            recurr(n,k,ind+1,l)
            l.pop()
            return
        recurr(n,k,1,[])
        return mainResult
            
                

        