class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sdict={}
        tdict={}
        for i in s:
            if i not in sdict:
                sdict[i]=1
            else:
                sdict[i]+=1
        for i in t:
            if i not in tdict:
                tdict[i]=1
            else:
                tdict[i]+=1
        for i in sdict:
            if i not in tdict:
                return False
            if sdict[i]!=tdict[i]:
                return False
        for i in tdict:
            if i not in sdict:
                return False
            if sdict[i]!=tdict[i]:
                return False
        return True

        