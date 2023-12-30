class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d={}
        sortedArray=[]
        for i in strs:
            sortedArray.append("".join(sorted(i)))
        # print(sortedArray,strs)
        for i in range(len(sortedArray)):
            if sortedArray[i] in d:
                d[sortedArray[i]].append(strs[i])
            else:
                d[sortedArray[i]]=[strs[i]]
        # print(d)
        return d.values()
        