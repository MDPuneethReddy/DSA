class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # space-o(n) time- o(nlogn)
        # d={}
        # sortedArray=[]
        # for i in strs:
        #     sortedArray.append("".join(sorted(i)))
        # # print(sortedArray,strs)
        # for i in range(len(sortedArray)):
        #     if sortedArray[i] in d:
        #         d[sortedArray[i]].append(strs[i])
        #     else:
        #         d[sortedArray[i]]=[strs[i]]
        # # print(d)
        # return d.values()
        d={}
        for i in strs:
            c=[0]*26
            for j in i:
                c[ord(j)-ord("a")]+=1
            if tuple(c) not in d:
                d[tuple(c)]=[i]
            else:
                d[tuple(c)].append(i)
        return d.values()
        