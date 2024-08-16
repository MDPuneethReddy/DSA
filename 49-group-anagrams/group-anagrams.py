class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d={}
        for i in strs:
            v=sorted(i)
            if tuple(v) not in d:
                d[tuple(v)]=[i]
            else:
                d[tuple(v)].append(i)
        l=[]
        for i in d:
            l.append(d[i])
        return l
        