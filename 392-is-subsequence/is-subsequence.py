class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        #timecomplexity- o(n)
        #space-o(1)
        counter1=0
        counter2=0
        while(counter1<len(s) and counter2<len(t)):
            if s[counter1]==t[counter2]:
                counter1+=1
                counter2+=1
            else:
                counter2+=1
        if counter1==len(s):
            return True
        else:
            return False

        