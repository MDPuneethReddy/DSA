class Solution:
    def longestPalindrome(self, s: str) -> str:
        def isPalindrome(string):
            # if string=="bb":
            #     print(string)
            start=0
            end=len(string)-1
            while(start<end):
                # if string=="bb":
                #     print(start,end,s[start],s[end])
                if string[start]==string[end]:
                    start+=1
                    end-=1
                else:
                    return False
            return True
            # if(string==string[::-1]):
            #     return True
            # else:
            #     return False
        c=0
        value=""
        for i in range(len(s)):
            start=i
            end=i
            while(start>=0 and end<=len(s)-1 and s[start]==s[end]):
                if((end-start+1)>c):
                    value=s[start:end+1]
                    c=end-start+1
                start-=1
                end+=1

            start=i
            end=i+1
            while(start>=0 and end<=len(s)-1 and s[start]==s[end]):
                if((end-start+1)>c):
                    value=s[start:end+1]
                    c=end-start+1
                start-=1
                end+=1

        return value

        # babad
        # i=0, 
        # start=0, end=0




        