class Solution:
    def longestPalindrome(self, s: str) -> str:
        def isPalindrome(string):
            if(string==string[::-1]):
                return True
            else:
                return False
        c=0
        value=""
        if len(s)==0:
            return ""
        if len(s)==1:
            return s
        for i in range(len(s)):
            for j in range(i+1,len(s)+1):
                if(isPalindrome(s[i:j])):
                    # print(s[i:j])
                    if(len(s[i:j])>c):
                        c=len(s[i:j])
                        value=s[i:j]
        return value



        