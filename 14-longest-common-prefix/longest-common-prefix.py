class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        value=strs[0]
        for i in range(1,len(strs)):
            j=0
            k=0
            l1=len(value)
            l2=len(strs[i])
            while(j<l1 and k<l2):
                # print(value[j],strs[i][k])
                if value[j]==strs[i][k]:
                    j+=1
                    k+=1
                else:
                    value=value[:j]
                    break
            value=value[:j]
        return value

        