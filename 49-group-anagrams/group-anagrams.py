class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d={}
        for i in strs:
            l=[0]*26
            for j in i:
                l[ord(j)-97]+=1
            l=tuple(l)
            if l in d:
                d[l].append(i)
            else:
                d[l]=[i]
        # print(d)
        return [d[i] for i in d]
        
        