class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i=0
        j=0
        k=0
        l1=len(word1)
        l2=len(word2)
        ms=""
        while(i<l1 and j<l2):
            if k%2==0:
                ms+=word1[i]
                i+=1
            else:
                ms+=word2[j]
                j+=1
            k+=1
            
        if i!=l1:
            ms+="".join(v for v in word1[i:l1])
        if j!=l2:
            ms+="".join(v for v in word2[j:l2])
        return ms

        