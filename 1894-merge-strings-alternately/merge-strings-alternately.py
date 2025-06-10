class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        #timecomplexity - o(n+m)
        #spacecomplexity- o(1)
        mergedString=""
        counter1=0
        counter2=0
        oddOrEvenCounter=True
        while(counter1<len(word1) and counter2<len(word2)):
            if oddOrEvenCounter:
                mergedString+=word1[counter1]
                counter1+=1
                oddOrEvenCounter=False
            else:
                mergedString+=word2[counter2]
                counter2+=1
                oddOrEvenCounter=True
        if(counter1<len(word1)):
            mergedString+=word1[counter1:]
        if(counter2<len(word2)):
            mergedString+=word2[counter2:]
        return mergedString


        